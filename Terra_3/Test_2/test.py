from qiskit.circuit.library import QuantumVolume
from qiskit.test.mock import FakeParis

qc = QuantumVolume(7, seed=42424242)
tqc = transpile(qc, backend=backend, translation_method='synthesis')
print(tqc.count_ops())