test = SummedOp([(Z ^ Z), (Y ^ I)]).reduce()
test = ~StateFn(test)
test.primitive.to_pauli_op()