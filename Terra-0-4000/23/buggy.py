from qiskit import *
qc = QuantumCircuit(1,1)
qc.qregs[0].name = "a_b_c"
qc.draw(output='mpl')
