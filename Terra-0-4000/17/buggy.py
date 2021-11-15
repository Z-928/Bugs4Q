from qiskit import Aer, QuantumCircuit, QuantumRegister, execute
from qiskit.circuit import Parameter

# create m = 2 circuits
qr = QuantumRegister(1)
quantum_circuit_1 = QuantumCircuit(qr)
quantum_circuit_2 = QuantumCircuit(qr)

theta = Parameter('theta')

# add parametrized gates
quantum_circuit_1.u3(theta, 0, 0, qr[0])
quantum_circuit_2.u3(theta, 3.14, 0, qr[0])

circuits = [quantum_circuit_1, quantum_circuit_2]

# inspect parameters property
for circuit in circuits:
    print(circuit.parameters)

# bind parameter to n = 1 values
job = execute(circuits,
              Aer.get_backend('qasm_simulator'),
              shots=512,
              parameter_binds=[{theta: 1}])

# AerError: 'Number of input circuits does not match number of input parameter bind dictionaries'
