import cirq
import numpy as np

qubits = [cirq.GridQubit(0,0), cirq.GridQubit(0,1)]
circuit = cirq.Circuit([cirq.ry(np.pi/2).on(qubits[0]),
                        cirq.ISWAP(qubits[0], qubits[1]) ** 0.5,
                        cirq.ry(np.pi/2).on(qubits[1])])

print(circuit)
qubits = [cirq.GridQubit(1,1), cirq.GridQubit(1,2)]
circuit2 = cirq.Circuit([cirq.ry(np.pi/2).on(qubits[0]),
                        cirq.ISWAP(qubits[0], qubits[1]) ** 0.5,
                        cirq.ry(np.pi/2).on(qubits[1])])
circuit2.append(circuit, strategy=cirq.InsertStrategy.EARLIEST)
print()
print()
print(circuit2)

circuit3 = cirq.Circuit([cirq.ry(np.pi/2).on(qubits[0]),
                        cirq.ISWAP(qubits[0], qubits[1]) ** 0.5,
                        cirq.ry(np.pi/2).on(qubits[1])])

circuit3.insert(0, circuit, strategy=cirq.InsertStrategy.EARLIEST)
print()
print()
print(circuit3)
