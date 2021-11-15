from qiskit.circuit import QuantumCircuit
from qiskit import Aer,transpile

c = QuantumCircuit(2)
simulator = Aer.get_backend('qasm_simulator')
c = transpile(c, simulator)
result = simulator.run(c).result()
plot_histogram(counts, title='Counts')