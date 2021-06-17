qr = QuantumRegister(3)
cr = ClassicalRegister(3)
circ = QuantumCircuit(qr, cr)

circ.cz(qr[0], qr[1])
circ.ccx(qr[0], qr[1], qr[2])
