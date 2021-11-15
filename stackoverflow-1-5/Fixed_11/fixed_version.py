import qiskit
from qiskit import *
from qiskit import IBMQ
qr = QuantumRegister(2)
cr = ClassicalRegister(2)
qc = QuantumCircuit(qr, cr)
%matplotlib inline
qc.draw(output='mpl')
qc.h(0)
qc.draw(output='mpl')