from qiskit import ClassicalRegister, QuantumRegister
from qiskit import QuantumCircuit, compile, register
register()

q = QuantumRegister(5)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)

qc.h(q[0])
qc.h(q[1])
qc.h(q[2])
qc.h(q[3])
qc.h(q[4])
qc.cx(q[0], q[1])
qc.cx(q[1], q[3])
qc.cx(q[1], q[4])
qc.cx(q[1], q[3])
qc.measure(q[4], c[1])
qc.measure(q[0], c[0])

seed = 213
qobj = compile(qc, 'ibmqx5', seed=seed)
