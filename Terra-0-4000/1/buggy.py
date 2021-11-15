from qiskit.aqua.operators import *

op =   Z @ X
eop = EvolvedOp(op)
circop = PauliTrotterEvolution().convert(eop)
circop.reduce()
circ = circop.to_circuit()
print(circ)


