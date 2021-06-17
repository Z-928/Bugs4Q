from qiskit import *

qr = QuantumRegister(5)
cr = ClassicalRegister(3)
circuit = QuantumCircuit(qr, cr)
circuit.x(qr[4])
circuit.measure(qr[1], cr[0])
circuit.measure(qr[3], cr[1])
circuit.measure(qr[4], cr[2])

backend = BasicAer.get_backend('qasm_simulator')
job = execute(circuit, backend)
result = job.result()
counts1 = result.get_counts()
print(counts1)

backend = Aer.get_backend('qasm_simulator')
job = execute(circuit, backend)
result = job.result()
counts2 = result.get_counts()
print(counts2)
