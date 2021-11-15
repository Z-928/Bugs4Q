from qiskit import *
from qiskit.quantum_info import Statevector
qc = QuantumCircuit(2)
st0 = Statevector.from_instruction(qc) 
qc.h(0)
st1 = Statevector.from_instruction(qc)
qc.cnot(0, 1)
st2 = Statevector.from_instruction(qc)

print(st0)
print(st1)
print(st2)


Statevector([1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j],
        dims=(2, 2))
Statevector([0.70710678+0.j, 0.70710678+0.j, 0.             +0.j,
         0.        +0.j],
        dims=(2, 2))
Statevector([0.70710678+0.j, 0.        +0.j, 0.        +0.j,
         0.70710678+0.j],
        dims=(2, 2))