from qiskit import *
from qiskit.visualization import plot_histogram
q = QuantumRegister(3)
c = ClassicalRegister(3)
circuit = QuantumCircuit(q, c)

# entangle cubit 1 & 2

circuit.h(1)

circuit.cx(1, 2)

# apply CNOT to qubit we want to send
circuit.cx(0, 1)

circuit.h(0)

circuit.measure([0,1], [0,1])

circuit.z(q[2]).c_if(c[0],1)

circuit.x(q[2]).c_if(c[1],1)

qc.measure([2], [2])

backend = Aer.get_backend('qasm_simulator')
job = execute(circuit, backend, shots=1024)
result = job.result()

counts = result.get_counts(circuit)
print(counts)
plot_histogram(counts)
