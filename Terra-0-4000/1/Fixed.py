op = -1j * (Z @ X)
eop = EvolvedOp(op)
circop = PauliTrotterEvolution().convert(eop)
circop.reduce()
circ = circop.to_circuit()
print(circ)

