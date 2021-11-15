from qiskit import *

q = QuantumRegister(2)
subnode = QuantumRegister(2)
qc = QuantumCircuit(q,subnode)
qc.ccx(subnode[0], subnode[1], q[1])
if (q[1] ==1) : 
    qc.x(q[0])
qc.x(q[1]) 
qc.ccx(subnode[0], subnode[1], q[1])
qc.draw()
