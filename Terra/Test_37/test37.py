q1 = QuantumRegister(3, 'q1')
c1 = ClassicalRegister(3, 'c1')
qc = QuantumCircuit(q1, c1)
qc.x(q1[0]).c_if(c1, 2)
circuit_drawer(qc, style={"reversebits": True})
