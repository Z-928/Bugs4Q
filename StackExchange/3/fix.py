from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import *



from qiskit import execute, BasicAer, Aer

qubit = QuantumRegister(1, 'qubit')
circuit = QuantumCircuit(qubit)

circuit.x(qubit)
circuit.barrier(qubit)
circuit.id(qubit)
circuit.barrier(qubit)
circuit.rx(3.1416, qubit)

backend = Aer.get_backend('statevector_simulator')
job = execute(circuit, backend)
result = job.result()
outputstate = result.get_statevector(circuit, decimals=3)
print(outputstate)
