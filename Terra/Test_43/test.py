q = QuantumRegister(2, "q")
qc = QuantumCircuit(q)
qc.cx(q[0],q[1])
qc.barrier(q)
circuit_drawer(qc)
