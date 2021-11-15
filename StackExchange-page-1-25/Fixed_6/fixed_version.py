import qiskit
from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import AerSimulator
from qiskit.providers.aer.noise import NoiseModel, coherent_unitary_error
import qiskit.quantum_info as qi
from qiskit.visualization import array_to_latex

epsilon = 0.1

err_h = QuantumCircuit(1, 1)
err_h.h(0)
err_h.p(epsilon, 0)
err_h.h(0)
err_h.p(-epsilon, 0)

u_err_h = qi.Operator(err_h)

noise_model = NoiseModel()
noise_model.add_all_qubit_quantum_error(coherent_unitary_error(u_err_h), 'h')
print(noise_model)
noise_sim = AerSimulator(noise_model=noise_model)

circ = QuantumCircuit(1, 1)
circ.h(0)
circ.h(0)
circ.measure(0, 0)

nshots = 10000
job = noise_sim.run(circ, shots=nshots)

job.result().get_counts()['0']/nshots