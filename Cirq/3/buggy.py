import cirq
import numpy as np

qubits = cirq.LineQubit.range(2)

circuit = cirq.Circuit()

circuit.append(cirq.X(qubits[0]))
circuit.append(cirq.Z(qubits[1]))

s = cirq.DensityMatrixSimulator()

results = s.simulate(circuit)

r = cirq.DensityMatrixSimulator()

circuit2 = cirq.Circuit()

circuit2.append(cirq.X(qubits[0]))

circuit2.append(cirq.Z(qubits[1]))

results2 =r.simulate(circuit2, initial_state = results._final_simulator_state.density_matrix)
