H2 = (-1.052373245772859 * I ^ I) + \
        (0.39793742484318045 * I ^ Z) + \
        (-0.39793742484318045 * Z ^ I) + \
        (-0.01128010425623538 * Z ^ Z) + \
        (0.18093119978423156 * X ^ X)

optimizer = AQGD(maxiter=10)
var_form = EfficientSU2(2, su2_gates=['ry', 'rz'], entanglement='linear', reps=2)
op1 = ~StateFn(H2) @ CircuitStateFn(primitive=var_form, coeff=1.)
op2 = ~StateFn((H2 @ H2).reduce()) @ CircuitStateFn(primitive=var_form, coeff=1.)
op = 3 * op1 - 4 * op2
grad = Gradient().convert(operator = op, params = list(var_form.parameters))

vqe = VQE(var_form, optimizer, gradient=grad,
            quantum_instance=Aer.get_backend('aer_simulator_statevector'))
result = vqe.compute_minimum_eigenvalue(operator=H2)