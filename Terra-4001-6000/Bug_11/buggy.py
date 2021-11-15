from qiskit import *
qc = QuantumCircuit(1)
qc.u1(0.24,0)
print(qc.decompose())
