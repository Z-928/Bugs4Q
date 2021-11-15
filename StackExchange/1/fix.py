from qiskit import *
from qiskit.visualization import circuit_drawer
#definitions
c = [ ClassicalRegister(1) for _ in range(2) ]
q = QuantumRegister(1)
qc = QuantumCircuit(q)
for register in c:
    qc.add_register( register )
    qc.h(q)
qc.measure(q,c[0])
qc.x(q[0]).c_if(c[0], 0)
qc.measure(q,c[1])
circuit_drawer(qc)
