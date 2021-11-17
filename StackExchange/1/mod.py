#change
q = QuantumRegister(1)
c = ClassicalRegister(2)
qc = QuantumCircuit(q,c)

# building the circuit
qc.h(q)
qc.measure(q[0],c[0])
qc.x(q[0]).c[0]_if(c[0], 0)
qc.measure(q[0],c[1])

#to
c = [ ClassicalRegister(1) for _ in range(2) ]
q = QuantumRegister(1)
qc = QuantumCircuit(q)
for register in c:
    qc.add_register( register )
    qc.h(q)
qc.measure(q,c[0])
qc.x(q[0]).c_if(c[0], 0)
qc.measure(q,c[1])
