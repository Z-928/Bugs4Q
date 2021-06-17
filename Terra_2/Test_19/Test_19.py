from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer, BasicAer, execute

qr1 = QuantumRegister(1, 'q1')
qr2 = QuantumRegister(1, 'q2')
cr = ClassicalRegister(4, 'c')
circuit2 = QuantumCircuit(qr1, qr2, cr)

circuit2.h(qr1)
circuit2.cx(qr1, qr2)
circuit2.measure(qr1, cr[0])
circuit2.measure(qr2, cr[1])
circuit2.measure(qr1, cr[2])
circuit2.measure(qr2, cr[3])

print(circuit2)

print("\nResult from BasicAer simulator:\n")
qk_backend = BasicAer.get_backend("qasm_simulator")
qk_job = execute(circuit2, backend=qk_backend, shots=1024)
qk_result = qk_job.result()
print(qk_result.get_counts(circuit2))

print("\nResult from Aer simulator:\n")
qk_backend = Aer.get_backend("qasm_simulator")
qk_job = execute(circuit2, backend=qk_backend, shots=1024)
qk_result = qk_job.result()
print(qk_result.get_counts(circuit2))
