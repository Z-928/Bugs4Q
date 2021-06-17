qreg = QuantumRegister(3, name='q')
creg1 = ClassicalRegister(3, name='c1')
creg2 = ClassicalRegister(2, name='c2')
qc = QuantumCircuit(qreg, creg1, creg2)

qc.measure(qreg, creg1)
qc.x(qreg[0]).c_if(creg1, 3)
