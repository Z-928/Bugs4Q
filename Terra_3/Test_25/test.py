from qiskit.quantum_info import Operator
from qiskit.extensions import HamiltonianGate
import numpy
 
# Create a circuit, exp(-i Z^Z)
c0 = HamiltonianGate(numpy.array([[ 1.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
        [ 0.+0.j, -1.+0.j,  0.+0.j,  0.+0.j],
        [ 0.+0.j,  0.+0.j, -1.+0.j,  0.+0.j],
        [ 0.+0.j,  0.+0.j,  0.+0.j,  1.+0.j]]),
 1.0).definition

# Rewrite with different gates
c1 = c0.decompose()

# The matrix representation should be the same
print(numpy.allclose(Operator(c0).data, Operator(c1).data))