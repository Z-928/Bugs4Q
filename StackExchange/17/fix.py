from qiskit.circuit.random import random_circuit

qr = random_circuit(10, 10, max_operands=3, measure=True)
qr.draw()
