import qiskit
from qiskit import *
from qiskit import IBMQ
qr = QuantumRegister(2)
cr = ClassicalRegister(2)
circuit = QuantumCircuit(qr, cr)
%matplotlib inline
circuit.draw(output='mpl')
circuit.h(qr(0))