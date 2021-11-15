from qiskit import *
#definitions
q = QuantumRegister(1)
c = ClassicalRegister(2)
qc = QuantumCircuit(q,c)

# building the circuit
qc.h(q)
qc.measure(q[0],c[0])
qc.x(q[0]).c[0]_if(c[0], 0)
qc.measure(q[0],c[1])
circuit_drawer(qc)
