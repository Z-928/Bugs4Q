# Imports
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
from qiskit import IBMQ
from qiskit.quantum_info.operators.pauli import Pauli
from qiskit.aqua.operators import *
from qiskit.aqua.operators.op_converter import to_matrix_operator
from qiskit import BasicAer
from scipy.linalg import eig

# Define a basic circuit
q = QuantumRegister(2, name='q')
qc = QuantumCircuit(q)
qc.rx(10.9891251356965,0)
qc.rx(6.286692023269373,1)
qc.rz(7.848801398269382, 0)
qc.rz(9.42477796076938,1)
qc.cx(0,1)
qc.draw()

# Define the Hamiltonian
pauli_string = []
pauli_string.append([1.0, Pauli.from_label('XX')])
pauli_string.append([-1.0, Pauli.from_label('YY')])
pauli_string.append([-1.0, Pauli.from_label('ZZ')])
H = WeightedPauliOperator(pauli_string)

# Show the Hamiltonian and compute its spectrum with exact diagonalization
Hmatrix = to_matrix_operator(H)
eigvals = eig(Hmatrix.dense_matrix)[0]
print("Hamiltonian: " + H.print_details())
print("Eigenvalues: " + str(eigvals))

# Output obtained:
# Hamiltonian: XX	(1+0j)
# YY	(-1+0j)
# ZZ	(-1+0j)

# Eigenvalues: [ 1.+0.j -3.+0.j  1.+0.j  1.+0.j]

# Now we measure the expectation value using built-in Qiskit functionality
evaluation_circuits = H.construct_evaluation_circuit(qc, False)
backend = BasicAer.get_backend('qasm_simulator')
job = execute(evaluation_circuits, backend, shots=1024)
# Evaluate the results
expectation_value, standard_deviation = H.evaluate_with_result(job.result(), False)
print("Expectation value: " + str(expectation_value) + " +- " + str(standard_deviation))

# Output obtained:
# Expectation value: (-3+0j) +- 0j

# Define the Hamiltonian but this time we split each of the terms in a sum of twice the identical part
pauli_string = []
pauli_string.append([0.5, Pauli.from_label('XX')])
pauli_string.append([-0.5, Pauli.from_label('YY')])
pauli_string.append([-0.5, Pauli.from_label('ZZ')])
pauli_string.append([0.5, Pauli.from_label('XX')])
pauli_string.append([-0.5, Pauli.from_label('YY')])
pauli_string.append([-0.5, Pauli.from_label('ZZ')])
H2 = WeightedPauliOperator(pauli_string)

# Show the Hamiltonian and compute its spectrum with exact diagonalization
Hmatrix2 = to_matrix_operator(H2)
eigvals2 = eig(Hmatrix2.dense_matrix)[0]
print("Hamiltonian: " + H2.print_details())
print("Eigenvalues: " + str(eigvals2))

# Output obtained:
# Hamiltonian: XX	(1+0j)
# YY	(-1+0j)
# ZZ	(-1+0j)

# Eigenvalues: [ 1.+0.j -3.+0.j  1.+0.j  1.+0.j]

# Now we measure the expectation value using built-in Qiskit functionality
evaluation_circuits2 = H2.construct_evaluation_circuit(qc, False)
backend2 = BasicAer.get_backend('qasm_simulator')
job2 = execute(evaluation_circuits2, backend2, shots=1024)
# Evaluate the results
expectation_value2, standard_deviation2 = H2.evaluate_with_result(job2.result(), False)
print("Expectation value: " + str(expectation_value2) + " +- " + str(standard_deviation2))

# Output obtained:
# Expectation value: (-6+0j) +- 0j <-- twice the correct result
