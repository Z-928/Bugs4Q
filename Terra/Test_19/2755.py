import numpy as np
from qiskit import QuantumCircuit, execute, BasicAer
from qiskit.quantum_info.operators.predicates import matrix_equal

# U3 gate params
a, b, c = 0.2, 0.3, 0.4

# U3 gate
circ1 = QuantumCircuit(1)
circ1.u3(a, b, c, 0)

# CU3 gate
circ2= QuantumCircuit(2)
circ2.cu3(a, b, c, 0, 1)

job = execute([circ1, circ2], BasicAer.get_backend('unitary_simulator'))
result = job.result()

# Circuit unitaries
mat_u3 = result.get_unitary(0)
mat_cu3 = result.get_unitary(1)

# Target Controlled-U3 unitary
target = np.kron(mat_u3, np.diag([0, 1])) + np.kron(np.eye(2), np.diag([1, 0]))

matrix_equal(target, mat_cu3, ignore_phase=True) 
