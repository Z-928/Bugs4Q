from qiskit import *
qub=QuantumRegister(5)
clreg=ClassicalRegister(2)
c=QuantumCircuit(qub,clreg)
cx(qub[0])#initialize(init_st,qub[0])
cx(qub[1])
c.cx(qub[ 0],qub[1])
c.measure(qub[:2],clreg)

backend=provider.get_backend('ibmq_burlington')
layout=Layout({qub[0]:3,qub[1]:4,qub[2]:0,qub[3]:1,qub[4]:2} )#,2:c[2],3:c[3],4:c[4]}
job = qiskit.execute(transpile(c,backend), backend, initial_layout=layout, shot=2048)
