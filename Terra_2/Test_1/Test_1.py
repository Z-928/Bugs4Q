from qiskit import *

qr1 = QuantumRegister(1, 'q1')
qr2 = QuantumRegister(1, 'q2')
cr = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qr2, qr1, cr)

print('Qubit ordering:', circuit.qubits)
print('Classical bit ordering:', circuit.clbits)

circuit.h(1)
circuit.measure(1,[cr[0],1])
