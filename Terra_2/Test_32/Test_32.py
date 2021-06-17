import math

from qiskit import QuantumCircuit
from qiskit import QuantumRegister
from qiskit import transpiler


def build_model_circuit(qreg, circuit=None):
    """Create quantum fourier transform circuit on quantum register qreg."""
    if circuit is None:
        circuit = QuantumCircuit(qreg, name="qft")

    n = len(qreg)

    for i in range(n):
        for j in range(i):
            circuit.cu1(math.pi/float(2**(i-j)), qreg[i], qreg[j])
        circuit.h(qreg[i])

    return circuit

n_qubits = 8
qr = QuantumRegister(n_qubits)
circuit = build_model_circuit(qr)

# Manually pulled configuration for melbourne
coupling_map = [[1, 0], [1, 2], [2, 3], [4, 3], [4, 10], [5, 4],
                [5, 6], [5, 9], [6, 8], [7, 8], [9, 8], [9, 10],
                [11, 3], [11, 10], [11, 12], [12, 2], [13, 1],
                [13, 12]]
transpiler.transpile(circuit,
                     basis_gates=['u1', 'u2', 'u3', 'cx', 'id'],
                     coupling_map=coupling_map)
