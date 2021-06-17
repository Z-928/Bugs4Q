from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import BasicAer, Aer, execute
basicaer = BasicAer.get_backend('qasm_simulator')
aer = Aer.get_backend('qasm_simulator')
qr = QuantumRegister(2)
cr = ClassicalRegister(1)
qc = QuantumCircuit(qr, cr)
qc.h(qr[0])
qc.x(qr[1])
qc.measure(qr[1], cr[0])

basicaer_result = execute(qc, backend=basicaer).result().get_counts()
aer_result = execute(qc, backend=aer).result().get_counts()

print(basicaer_result)
print(aer_result)
