from qiskit import *
circuit1 = QuantumCircuit(1,1)
circuit1.u(pi/2, pi/3, pi/4, 0)
simulator = Aer.get_backend("unitary_simulator")
result = execute(circuit1, backend=simulator).result()
unitary = result.get_unitary()
print(unitary)
