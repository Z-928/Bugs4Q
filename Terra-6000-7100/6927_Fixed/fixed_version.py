from qiskit import Aer, QuantumCircuit, transpile
from qiskit.circuit.library import PhaseEstimation
qc= QuantumCircuit(3,3)
# dummy unitary circuit
unitary_circuit = QuantumCircuit(1)
unitary_circuit.h(0)
# QPE
qc.append(PhaseEstimation(2, unitary_circuit), list(range(3)))
qc.measure(list(range(3)), list(range(3)))
backend = Aer.get_backend('qasm_simulator')
qc_transpiled = transpile(qc, backend)
result = backend.run(qc, shots = 8192).result()