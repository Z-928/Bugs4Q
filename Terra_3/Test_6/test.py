import sys
import numpy as np
import qiskit
from qiskit import QuantumRegister, QuantumCircuit, Aer, execute, ClassicalRegister
from qiskit.aqua.algorithms import AmplitudeEstimation
from qiskit.aqua.operators import CircuitOp, Zero, One
from qiskit.tools.visualization import plot_histogram
import matplotlib.pyplot as plt

theta = 0.65
m = 5 #number of evaluation qubits

q = QuantumRegister(1, 'q') # objective qubit
ae_q = QuantumRegister(m, 'm') # AE output register
c = ClassicalRegister(m, 'c')
qc = QuantumCircuit(q, ae_q)#, c)

# State preparation circuit
qc2 = QuantumCircuit(q) 
qc2.ry(theta, q[0])

# Forward AE
ae = AmplitudeEstimation(m, state_preparation=qc2, objective_qubits=[0])
ae_inst = ae.construct_circuit().to_instruction()
qc.append(ae_inst, list(ae_q) + list(q))

#Reverse AE
ae_inst_r = ae.construct_circuit().inverse().to_instruction()
qc.append(ae_inst_r, list(ae_q) + list(q))

#qc.measure(ae_q, c)
qc.decompose().draw()
qc_op = CircuitOp(qc)
print("<0|U^dg U|0> = {}".format((~Zero @  qc_op @ Zero).eval()))
print("<0|U^dg U|0> = {}".format((~Zero @ (qc_op @ Zero).eval()).eval()))
print("<0|U^dg U|0> = {}".format(((~Zero @ qc_op).eval() @ Zero).eval()))

import qiskit.tools.jupyter
%qiskit_version_table
%qiskit_copyright