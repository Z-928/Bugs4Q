from qiskit.algorithms import NumPyEigensolver, NumPyMinimumEigensolver
from qiskit.opflow import PauliSumOp

def test_exact_eigen(op):
    print(op)
    solver = NumPyMinimumEigensolver()
    print(solver.compute_minimum_eigenvalue(op).eigenvalue)

    solver = NumPyEigensolver(k=2)
    print(solver.compute_eigenvalues(op).eigenvalues)

    solver = NumPyEigensolver(k=1)
    print(solver.compute_eigenvalues(op).eigenvalues)
    print()

op = PauliSumOp.from_list([('XI', 1)])
test_exact_eigen(op)

op = PauliSumOp.from_list([('X', 1)])
test_exact_eigen(op)