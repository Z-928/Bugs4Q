from qiskit import QuantumRegister, QuantumCircuit, ClassicalRegister

qr = QuantumRegister(3)
cr = ClassicalRegister(1)
qc1 = QuantumCircuit(qr)

qc1.x(qr[1])
qc1.h(range(3))
qc1.cx(qr[1], qr[2])
qc1.cx(qr[0], qr[1])

style = {'gatefacecolor': '#fffffe'}

qc1.draw(output='mpl', style=style).show()
