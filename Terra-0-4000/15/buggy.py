


from qiskit import *
qc = QuantumCircuit(2,1)
qc.measure(1,0)
qc.h(1)
qc.cx(1,0)
qc.draw()

