import qiskit
from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import AerSimulator
from qiskit.providers.aer.noise import NoiseModel, coherent_unitary_error

epsilon = 0.1
z_rot = qiskit.circuit.library.U1Gate(epsilon)
z_rot_dg = qiskit.circuit.library.U1Gate(-epsilon)

noise_model = NoiseModel()
noise_model.add_all_qubit_quantum_error(coherent_unitary_error(z_rot), 'u2')
noise_model.add_all_qubit_quantum_error(coherent_unitary_error(z_rot), 'u3')
print(noise_model)
noise_sim = AerSimulator(noise_model=noise_model)

circ = QuantumCircuit(1, 1)
circ.h(0)
circ.h(0)
circ.measure(0, 0)

# change optimization level to 1 to turn off effect of channel
ct = transpile(circ, noise_sim, optimization_level=0) 
print(ct.draw())
nshots=10000
job = noise_sim.run(ct, shots=nshots)
print(job.result().get_counts()['0']/nshots)