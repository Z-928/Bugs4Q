
# https://github.com/Z-726/Bugs-from-Users/edit/main/Program/1999.py


import numpy as np
from qiskit import *
from qiskit.transpiler import transpile
from qiskit.tools.qi.qi import random_unitary_matrix
from qiskit.mapper import two_qubit_kak
from qiskit.mapper import CouplingMap
from qiskit.extensions.standard import SwapGate
from qiskit.converters import circuit_to_dag


def build_qv_circuit(seed, n, depth):
    """Create a quantum program containing model circuits.

    The model circuits consist of layers of Haar random
    elements of SU(4) applied between corresponding pairs
    of qubits in a random bipartition.

    name = leading name of circuits
    n = number of qubits
    depth = ideal depth of each model circuit (over SU(4))

    """
    np.random.seed(seed)
    q = QuantumRegister(n, "q")
    c = ClassicalRegister(n, "c")
    # Create measurement subcircuit
    qc = QuantumCircuit(q,c)
    # For each layer
    for j in range(depth):
        # Generate uniformly random permutation Pj of [0...n-1]
        perm = np.random.permutation(n)
        # For each pair p in Pj, generate Haar random SU(4)
        # Decompose each SU(4) into CNOT + SU(2) and add to Ci
        for k in range(int(np.floor(n/2))):
            qubits = [int(perm[2*k]), int(perm[2*k+1])]
            U = random_unitary_matrix(4)
            for gate in two_qubit_kak(U):
                i0 = qubits[gate["args"][0]]
                if gate["name"] == "cx":
                    i1 = qubits[gate["args"][1]]
                    qc.cx(q[i0], q[i1])
                elif gate["name"] == "u1":
                    qc.u1(gate["params"][2], q[i0])
                elif gate["name"] == "u2":
                    qc.u2(gate["params"][1], gate["params"][2],
                                 q[i0])
                elif gate["name"] == "u3":
                    qc.u3(gate["params"][0], gate["params"][1],
                                 gate["params"][2], q[i0])
                elif gate["name"] == "id":
                    pass  # do nothing
    #qc.measure(q,c)
    return qc

circuit =  build_qv_circuit(1234, 20, 100)
dag = circuit_to_dag(circuit)
print(dag.num_tensor_factors())
