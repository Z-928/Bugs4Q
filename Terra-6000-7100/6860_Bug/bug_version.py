import qiskit

qreg = qiskit.QuantumRegister(1)
circuit = qiskit.QuantumCircuit(qreg)

circuit._qubits = []
circuit.qregs = []

circuit.add_register(qreg)

print(circuit.qregs)
print(circuit.qubits)