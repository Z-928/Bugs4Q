from qiskit import *
from qiskit.circuit import Parameter

alpha = Parameter('alpha')
qc = QuantumCircuit(1)
qc.p(alpha, 0)
qc.qasm(True)