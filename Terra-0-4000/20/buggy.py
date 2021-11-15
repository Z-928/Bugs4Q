
from qiskit import *

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.rx(1+1j, 0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

qc.draw()
