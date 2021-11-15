import qiskit as qk
qr0 = qk.QuantumRegister(2, 'q0')
qr1 = qk.QuantumRegister(2, 'q1')
sorted(qr0[:])
sorted(qr1[:] + qr0[:])

