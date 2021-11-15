from qiskit.providers.aer import AerSimulator, QasmSimulator
from qiskit.algorithms import VQE
from qiskit.algorithms.optimizers import COBYLA 
from qiskit.circuit.library import TwoLocal
from qiskit import *
from qiskit.opflow import OperatorBase
from qiskit.opflow import Z, X, I  # Pauli Z, X matrices and identity
import pylab
import matplotlib.pyplot as plt
import numpy as np

H =   504.0 * I^I^I^I^I^I^I^Z+1008.0 * I^I^I^I^I^I^Z^I+2016.0 * I^I^I^I^I^Z^I^I+504.0 * I^I^I^I^Z^I^I^I+1143.7999999999997 * I^I^I^Z^I^I^I^I+2287.6 * I^I^Z^I^I^I^I^I+4575.200000000001 * I^Z^I^I^I^I^I^I+1143.7999999999997 * Z^I^I^I^I^I^I^I+98.0 * I^I^I^I^I^I^Z^Z+196.0 * I^I^I^I^I^Z^I^Z+392.0 * I^I^I^I^I^Z^Z^I+49.0 * I^I^I^I^Z^I^I^Z+98.0 * I^I^I^I^Z^I^Z^I+196.0 * I^I^I^I^Z^Z^I^I+93.1 * I^I^Z^Z^I^I^I^I+186.2 * I^Z^I^Z^I^I^I^I+372.4 * I^Z^Z^I^I^I^I^I+46.55 * Z^I^I^Z^I^I^I^I+93.1 * Z^I^Z^I^I^I^I^I+186.2 * Z^Z^I^I^I^I^I^I

backend = QasmSimulator()
optimizer = COBYLA(maxiter=2000)
ansatz = TwoLocal(num_qubits=8, rotation_blocks='ry', entanglement_blocks=None, entanglement='full', reps=1, skip_unentangled_qubits=False, skip_final_rotation_layer=False)
# set the algorithm
vqe = VQE(ansatz, optimizer, quantum_instance=backend)

#run it with the Hamiltonian we defined above
result = vqe.compute_minimum_eigenvalue(H) 