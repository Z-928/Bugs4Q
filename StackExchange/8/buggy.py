import numpy as np
from qiskit import execute, QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.providers.aer import QasmSimulator
from qiskit.tools.visualization import plot_histogram

# Qiskit Aer noise module imports
from qiskit.providers.aer.noise import NoiseModel
from qiskit.providers.aer.noise.errors import pauli_error

# System Specification
n_qubits = 2
circ = QuantumCircuit(n_qubits, n_qubits)

# Test Circuit
circ.h(0)
circ.rx(np.pi/4,1)
circ.cz(0,1)
circ.rz(np.pi,0)
circ.measure(range(n_qubits), range(n_qubits))

# Basis gates
basis_gates = ['id', 'h', 'rx', 'rz', 'cz']

# Example error probabilities
p = 0.05

# QuantumError objects
error_gate1 = pauli_error([('X',p), ('I', 1 - p)])
error_gate2 = error_gate1.tensor(error_gate1)

# Add errors to noise model
noise_bit_flip = NoiseModel(basis_gates)
noise_bit_flip.add_all_qubit_quantum_error(error_gate1, ["h", "rx","rz"])
noise_bit_flip.add_all_qubit_quantum_error(error_gate2, ["cz"])

print(noise_bit_flip)

# Backend
simulator = QasmSimulator()

# Run the noisy simulation
job = execute(circ, simulator,
              basis_gates = noise_bit_flip.basis_gates,
              noise_model = noise_bit_flip)
result_bit_flip = job.result()
counts_bit_flip = result_bit_flip.get_counts(0)

# Plot noisy output
plot_histogram(counts_bit_flip)
