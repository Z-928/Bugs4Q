from qiskit_aqua import Operator, run_algorithm, get_algorithm_instance
from qiskit_aqua.input import get_input_instance
from qiskit_aqua.algorithms.classical.cplex import stableset
import numpy as np
import networkx as nx

G = nx.gnp_random_graph(10, 0.567658261253)
w = nx.to_numpy_matrix(G)
qubitOp, offset = stableset.get_stableset_qubitops(w)
algo_input = get_input_instance('EnergyInput')
algo_input.qubit_op = qubitOp

if 1==1:
algorithm_cfg = {
'name': 'ExactEigensolver',
}

params = {
    'problem': {'name': 'ising'},
    'algorithm': algorithm_cfg
}
result = run_algorithm(params,algo_input)

x = stableset.sample_most_likely(result['eigvecs'][0])
print('energy:', result['energy'])
print('stable set objective:', result['energy'] + offset)
print('solution:', stableset.get_graph_solution(x))
print('solution objective and feasibility:', stableset.stableset_value(x, w))
if 1==1:
algorithm_cfg = {
'name': 'VQE',
'operator_mode': 'matrix'
}

optimizer_cfg = {
    'name': 'L_BFGS_B',
    'maxfun': 2000
}

var_form_cfg = {
    'name': 'RYRZ',
    'depth': 3,
    'entanglement': 'linear'
}

params = {
    'problem': {'name': 'ising'},
    'algorithm': algorithm_cfg,
    'optimizer': optimizer_cfg,
    'variational_form': var_form_cfg,
    'backend': {'name': 'local_statevector_simulator'}
}

result = run_algorithm(params,algo_input)

x = stableset.sample_most_likely(result['eigvecs'][0])
print('energy:', result['energy'])
print('time:', result['eval_time'])
print('stable set objective:', result['energy'] + offset)
print('solution:', stableset.get_graph_solution(x))
print('solution objective and feasibility:', stableset.stableset_value(x, w))
