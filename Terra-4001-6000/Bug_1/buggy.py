from qiskit import QuantumCircuit, transpile

qc = QuantumCircuit(1)
qc.initialize([1, 0], [0])
qc.inverse()
