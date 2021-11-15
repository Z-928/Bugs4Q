from qiskit import *
from math import pi
import numpy as np
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit.quantum_info.operators import Operator

circ = QuantumCircuit(3)
circ.crz(pi/2,2,0)
circ.crz(pi/4,2,1)
U = Operator(circ)

qae = QuantumRegister(2,'qae')
reg_b = QuantumRegister(2,'b')
qc = QuantumCircuit(qae,reg_b)
qc.append(U,[qae[0],reg_b[0],reg_b[1]])
uni = Operator(qc)
print(np.round(uni.data,1))
qc.draw('mpl')
