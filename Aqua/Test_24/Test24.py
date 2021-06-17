from qiskit.quantum_info import Pauli
from qiskit.aqua import Operator
import copy
aux = Operator(paulis=[(1.0,Pauli(label='II'))])
aux.to_matrix()
print('op1=',aux.matrix)
aux2 = Operator(paulis=[(1.0,Pauli(label='ZI'))])
aux2.to_matrix()
print('op2=',aux2.matrix)

print('---Out-of-place subtraction')
print(aux.matrix-aux2.matrix)
aux3 = aux - aux2
print(aux3.matrix)

print('---Out-of-place addition')
print(aux.matrix+aux2.matrix)
aux3 = aux + aux2
print(aux3.matrix)

print('---In-place subtraction')
aux3 = copy.deepcopy(aux)
print(aux3.matrix)
print(aux.matrix-aux2.matrix)
aux3 -= aux2
print(aux3.matrix)

print('---In-place addition')
aux3 = copy.deepcopy(aux)
print(aux3.matrix)
print(aux3.matrix+aux2.matrix)
aux3 += aux2
print(aux3.matrix)
