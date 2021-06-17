from qiskit.circuit import QuantumCircuit, Parameter
x = Parameter('x')
circuit = QuantumCircuit(1, global_phase=x)
circuit.bind_parameters({x: 2}).draw()