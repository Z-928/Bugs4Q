
   
#Delete
simulator = QasmSimulator()

#change
q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)
qc.measure(q,c)
qc.measure(q,c)

#to
q = QuantumRegister(2)
c1 = ClassicalRegister(2)
c2 = ClassicalRegister(2)
qc = QuantumCircuit(q, c1,c2)
qc.measure(q,c1)
qc.measure(q,c2)
