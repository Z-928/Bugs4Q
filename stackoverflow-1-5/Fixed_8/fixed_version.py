from qiskit.circuit import QuantumCircuit
from qiskit import Aer,transpile
from qiskit.compiler import assemble

c = QuantumCircuit(2)
simulator = Aer.get_backend('qasm_simulator')
c = transpile(c, simulator)
c = assemble(c)
result = simulator.run(c).result()




