#change

q = QuantumRegister(2)
subnode = QuantumRegister(2)
qc = QuantumCircuit(q,subnode)
qc.ccx(subnode[0], subnode[1], q[1])
if (q[1] ==1) : 
    qc.x(q[0])
qc.x(q[1]) 
qc.ccx(subnode[0], subnode[1], q[1])

#to

q = QuantumRegister(5)
c = ClassicalRegister(5)
qc = QuantumCircuit(q,c)

qc.ccx(q[0],q[1],q[3])
qc.ccx(q[2],q[3],q[4])
qc.ccx(q[0],q[1],q[3])
