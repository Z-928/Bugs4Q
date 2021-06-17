from qiskit import *
        
q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q,c)
qa = QuantumRegister(2)
ca = ClassicalRegister(2)
qca = QuantumCircuit(q,c)
print(qc.name)
print(q.name)
print(c.name)
print(qca.name)
print(qa.name)
print(ca.name)
