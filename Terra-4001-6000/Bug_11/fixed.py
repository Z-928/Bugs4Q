from qiskit import *
qc = QuantumCircuit(1)
qc.u1(0.24,0)
transpile(qc, basis_gates=['u1', 'u2', 'u3', 'cx'])
print(qc)
