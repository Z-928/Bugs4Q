from qiskit import *
q = QuantumRegister(5,name='q')
c = ClassicalRegister(5, name='c')
qc_bad = QuantumCircuit(q, c)

qc_bad.x(q[4])
for kk in range(5):
    qc_bad.h(q[kk])
qc_bad.barrier(q)
qc_bad.cx(q[2], q[4])
qc_bad.cx(q[3], q[4])

qc_bad.barrier(q)
qc_bad.cx(q[2], q[0])
qc_bad.h(q[2])
qc_bad.h(q[0])
qc_bad.cx(q[2], q[0])
qc_bad.h(q[2])
qc_bad.h(q[0])
qc_bad.cx(q[2], q[0])

qc_bad.draw(output='text')


