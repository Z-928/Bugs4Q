import qiskit as q
from qiskit.visualization import plot_histogram

circuit = q.QuantumCircuit(3, 3)

# entangle cubit 1 & 2

circuit.h(1)

circuit.cx(1, 2)

# apply CNOT to qubit we want to send
circuit.cx(0, 1)

circuit.h(0)

circuit.measure([0,1], [0,1])

circuit.cx(1, 2)

circuit.cz(0, 2)

print(circuit)

backend = q.Aer.get_backend('qasm_simulator')
job = q.execute(circuit, backend, shots=1024)
result = job.result()

counts = result.get_counts(circuit)
plot_histogram(counts)
