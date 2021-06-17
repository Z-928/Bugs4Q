# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""
The Truth Table-based Quantum Oracle.
"""

import logging
import operator
import math
import numpy as np
from functools import reduce
from dlx import DLX
from qiskit import QuantumRegister, QuantumCircuit
from qiskit.aqua import AquaError
from qiskit.aqua.circuits import ESOP
from qiskit.aqua.components.oracles import Oracle
from qiskit.aqua.utils.arithmetic import is_power_of_2
from ._pyeda_check import _check_pluggable_valid as check_pyeda_valid

logger = logging.getLogger(__name__)


def get_prime_implicants(ones=None, dcs=None):
    """
    Compute all prime implicants for a truth table using the Quine-McCluskey Algorithm

    Args:
        ones (list of int): The list of integers corresponding to '1' outputs
        dcs (list of int): The list of integers corresponding to don't-cares

    Return:
        list of lists of int, representing all prime implicants
    """

    def combine_terms(terms, num1s_dict=None):
        if num1s_dict is None:
            num1s_dict = {}
            for num in terms:
                num1s = bin(num).count('1')
                if num1s not in num1s_dict:
                    num1s_dict[num1s] = [num]
                else:
                    num1s_dict[num1s].append(num)

        new_implicants = {}
        new_num1s_dict = {}
        prime_dict = {mt: True for mt in sorted(terms)}
        cur_num1s, max_num1s = min(num1s_dict.keys()), max(num1s_dict.keys())
        while cur_num1s < max_num1s:
            if cur_num1s in num1s_dict and (cur_num1s + 1) in num1s_dict:
                for cur_term in sorted(num1s_dict[cur_num1s]):
                    for next_term in sorted(num1s_dict[cur_num1s + 1]):
                        if isinstance(cur_term, int):
                            diff_mask = dc_mask = cur_term ^ next_term
                            implicant_mask = cur_term & next_term
                        elif isinstance(cur_term, tuple):
                            if terms[cur_term][1] == terms[next_term][1]:
                                diff_mask = terms[cur_term][0] ^ terms[next_term][0]
                                dc_mask = diff_mask | terms[cur_term][1]
                                implicant_mask = terms[cur_term][0] & terms[next_term][0]
                            else:
                                continue
                        else:
                            raise AquaError('Unexpected type: {}.'.format(type(cur_term)))
                        if bin(diff_mask).count('1') == 1:
                            prime_dict[cur_term] = False
                            prime_dict[next_term] = False
                            if isinstance(cur_term, int):
                                cur_implicant = (cur_term, next_term)
                            elif isinstance(cur_term, tuple):
                                cur_implicant = tuple(sorted((*cur_term, *next_term)))
                            else:
                                raise AquaError('Unexpected type: {}.'.format(type(cur_term)))
                            new_implicants[cur_implicant] = (
                                implicant_mask,
                                dc_mask
                            )
                            num1s = bin(implicant_mask).count('1')
                            if num1s not in new_num1s_dict:
                                new_num1s_dict[num1s] = [cur_implicant]
                            else:
                                if cur_implicant not in new_num1s_dict[num1s]:
                                    new_num1s_dict[num1s].append(cur_implicant)
            cur_num1s += 1
        return new_implicants, new_num1s_dict, prime_dict

    terms = ones + dcs
    cur_num1s_dict = None

    prime_implicants = []

    while True:
        next_implicants, next_num1s_dict, cur_prime_dict = combine_terms(terms, num1s_dict=cur_num1s_dict)
        for implicant in cur_prime_dict:
            if cur_prime_dict[implicant]:
                if isinstance(implicant, int):
                    if implicant not in dcs:
                        prime_implicants.append((implicant,))
                else:
                    if not set.issubset(set(implicant), dcs):
                        prime_implicants.append(implicant)
        if next_implicants:
            terms = next_implicants
            cur_num1s_dict = next_num1s_dict
        else:
            break

    return prime_implicants


def get_exact_covers(cols, rows, num_cols=None):
    """
    Use Algorithm X to get all solutions to the exact cover problem

    https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X

    Args:
          cols (list of int): A list of integers representing the columns to be covered
          rows (list of list of int): A list of lists of integers representing the rows
          num_cols (int): The total number of columns

    Returns:
        All exact covers
    """
    if num_cols is None:
        num_cols = max(cols) + 1
    ec = DLX([(c, 0 if c in cols else 1) for c in range(num_cols)])
    ec.appendRows([[c] for c in cols])
    ec.appendRows(rows)
    exact_covers = []
    for s in ec.solve():
        cover = []
        for i in s:
            cover.append(ec.getRowList(i))
        exact_covers.append(cover)
    return exact_covers


class TruthTableOracle(Oracle):

    CONFIGURATION = {
        'name': 'TruthTableOracle',
        'description': 'Truth Table Oracle',
        'input_schema': {
            '$schema': 'http://json-schema.org/schema#',
            'id': 'truth_table_oracle_schema',
            'type': 'object',
            'properties': {
                'bitmaps': {
                    "type": "array",
                    "default": [],
                    "items": {
                        "type": "string"
                    }
                },
                "optimization": {
                    "type": "string",
                    "default": "off",
                    'enum': [
                        'off',
                        'qm-dlx'
                    ]
                },
                'mct_mode': {
                    'type': 'string',
                    'default': 'basic',
                    'enum': [
                        'basic',
                        'basic-dirty-ancilla',
                        'advanced',
                        'noancilla',
                    ]
                },
            },
            'additionalProperties': False
        }
    }

    def __init__(self, bitmaps, optimization='off', mct_mode='basic'):
        """
        Constructor for Truth Table-based Oracle

        Args:
            bitmaps (str or [str]): A single binary string or a list of binary strings representing the desired
                single- and multi-value truth table.
            optimization (str): Optimization mode to use for minimizing the circuit.
                Currently, besides no optimization ('off'), Aqua also supports a 'qm-dlx' mode,
                which uses the Quine-McCluskey algorithm to compute the prime implicants of the truth table,
                and then compute an exact cover to try to reduce the circuit.
            mct_mode (str): The mode to use when constructing multiple-control Toffoli.
        """
        if isinstance(bitmaps, str):
            bitmaps = [bitmaps]

        self.validate(locals())
        super().__init__()

        self._mct_mode = mct_mode
        self._optimization = optimization

        self._bitmaps = bitmaps

        # check that the input bitmaps length is a power of 2
        if not is_power_of_2(len(bitmaps[0])):
            raise AquaError('Length of any bitmap must be a power of 2.')
        for bitmap in bitmaps[1:]:
            if not len(bitmap) == len(bitmaps[0]):
                raise AquaError('Length of all bitmaps must be the same.')
        self._nbits = int(math.log(len(bitmaps[0]), 2))
        self._num_outputs = len(bitmaps)

        esop_exprs = []
        for bitmap in bitmaps:
            esop_expr = self._get_esop_ast(bitmap)
            esop_exprs.append(esop_expr)

        self._esops = [
            ESOP(esop_expr, num_vars=self._nbits) for esop_expr in esop_exprs
        ] if esop_exprs else None

        self.construct_circuit()

    @staticmethod
    def check_pluggable_valid():
        check_pyeda_valid(TruthTableOracle.CONFIGURATION['name'])

    def _get_esop_ast(self, bitmap):
        from pyeda.inter import exprvars, And, Xor
        v = exprvars('v', self._nbits)

        def binstr_to_vars(binstr):
            return [
                       (~v[x[1] - 1] if x[0] == '0' else v[x[1] - 1])
                       for x in zip(binstr, reversed(range(1, self._nbits + 1)))
                   ][::-1]

        if self._optimization == 'off':
            expression = Xor(*[
                And(*binstr_to_vars(term)) for term in
                [np.binary_repr(idx, self._nbits) for idx, v in enumerate(bitmap) if v == '1']])
        else:  # self._optimization == 'qm-dlx':
            ones = [i for i, v in enumerate(bitmap) if v == '1']
            if not ones:
                return ('const', 0,)
            dcs = [i for i, v in enumerate(bitmap) if v == '*' or v == '-' or v.lower() == 'x']
            pis = get_prime_implicants(ones=ones, dcs=dcs)
            cover = get_exact_covers(ones, pis)[-1]
            clauses = []
            for c in cover:
                if len(c) == 1:
                    term = np.binary_repr(c[0], self._nbits)
                    clause = And(*[
                        v for i, v in enumerate(binstr_to_vars(term))
                    ])
                elif len(c) > 1:
                    c_or = reduce(operator.or_, c)
                    c_and = reduce(operator.and_, c)
                    _ = np.binary_repr(c_and ^ c_or, self._nbits)[::-1]
                    clause = And(*[
                        v for i, v in enumerate(binstr_to_vars(np.binary_repr(c_and, self._nbits))) if _[i] == '0'
                    ])
                else:
                    raise AquaError('Unexpected cover term size {}.'.format(len(c)))
                if clause:
                    clauses.append(clause)
            expression = Xor(*clauses)

        raw_ast = expression.to_ast()
        idx_mapping = {
            u: v + 1 for u, v in zip(sorted(expression.usupport), [v.indices[0] for v in sorted(expression.support)])
        }

        if raw_ast[0] == 'and' or raw_ast[0] == 'or' or raw_ast[0] == 'xor':
            clauses = []
            for c in raw_ast[1:]:
                if c[0] == 'lit':
                    clauses.append(('lit', (idx_mapping[c[1]]) if c[1] > 0 else (-idx_mapping[-c[1]])))
                elif (c[0] == 'or' or c[0] == 'and') and (raw_ast[0] != c[0]):
                    clause = []
                    for l in c[1:]:
                        clause.append(('lit', (idx_mapping[l[1]]) if l[1] > 0 else (-idx_mapping[-l[1]])))
                    clauses.append((c[0], *clause))
                else:
                    raise AquaError('Unrecognized logic expression: {}'.format(raw_ast))
        elif raw_ast[0] == 'lit':
            return 'lit', idx_mapping[raw_ast[1]] if raw_ast[1] > 0 else -idx_mapping[-raw_ast[1]]
        elif raw_ast[0] == 'const':
            return raw_ast
        else:
            raise AquaError('Unrecognized root expression type: {}.'.format(raw_ast[0]))
        ast = (raw_ast[0], *clauses)
        return ast

    @property
    def variable_register(self):
        return self._variable_register

    @property
    def ancillary_register(self):
        return self._ancillary_register

    @property
    def output_register(self):
        return self._output_register

    def construct_circuit(self):
        if self._circuit is not None:
            return self._circuit
        self._circuit = QuantumCircuit()
        self._output_register = QuantumRegister(self._num_outputs, name='o')
        if self._esops:
            for i, e in enumerate(self._esops):
                if e is not None:
                    ci = e.construct_circuit(
                        output_register=self._output_register,
                        output_idx=i,
                        mct_mode=self._mct_mode
                    )
                    self._circuit += ci
            self._variable_register = self._ancillary_register = None
            for qreg in self._circuit.qregs:
                if qreg.name == 'v':
                    self._variable_register = qreg
                elif qreg.name == 'a':
                    self._ancillary_register = qreg
        else:
            self._variable_register = QuantumRegister(self._nbits, name='v')
            self._ancillary_register = None
            self._circuit.add_register(self._variable_register, self._output_register)
        return self._circuit

    def evaluate_classically(self, measurement):
        assignment = [(var + 1) * (int(tf) * 2 - 1) for tf, var in zip(measurement[::-1], range(len(measurement)))]
        ret = [bitmap[int(measurement, 2)] == '1' for bitmap in self._bitmaps]
        if self._num_outputs == 1:
            return ret[0], assignment
        else:
            return ret, assignment
