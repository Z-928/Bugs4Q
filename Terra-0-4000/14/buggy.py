from qiskit import QuantumRegister, QuantumCircuit
from qiskit.extensions import XGate, UnitaryGate

qr = QuantumRegister(2)
circ = QuantumCircuit(qr)
circ.append(XGate(), [qr[0]])
circ.append(XGate(label='alt-X'), [qr[0]])
circ.append(UnitaryGate([[1, 0, 0, 0],
                         [0, 0, 1j, 0],
                         [0, 1j, 1, 0],
                         [0, 0, 0, 1]], label="iswap"), [qr[0], qr[1]])
print(circ)
