import numpy as np
from qiskit import *

qc = QuantumCircuit(3)
qc.h(0)
qc.h(1)
qc.cp(np.pi/8,0,1)

qc.cp(np.pi/4,0,2)
trans_qc = transpile(qc, basis_gates=['id', 'rz', 'sx', 'x', 'cx'], optimization_level=2)
trans_qc.draw()