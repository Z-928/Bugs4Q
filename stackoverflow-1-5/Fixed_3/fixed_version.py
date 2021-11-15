from qiskit import *

qr = QuantumRegister(2)
cr = ClassicalRegister(2)

Qc = QuantumCircuit(qr,cr)

print ('This is the initial state')
Qc.draw('mpl').show()