from qiskit import *
circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)
result = execute(circuit, backend, shots=1000).result()
counts  = result.get_counts(circuit)
print(counts)
