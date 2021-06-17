from qiskit import execute
from qiskit.circuit.library import QFT
from qiskit.providers.aer import QasmSimulator
from qiskit.providers.aer.noise import NoiseModel, amplitude_damping_error

error1 = amplitude_damping_error(0.2)
noise_model = NoiseModel()
noise_model.add_all_qubit_quantum_error(error1, ['id', 'u1', 'u2', 'u3'])
noise_model.add_all_qubit_quantum_error(error1.tensor(error1), ['cx'])

backend = QasmSimulator(method='matrix_product_state', noise_model=noise_model)

job = execute(QFT(5), backend)
