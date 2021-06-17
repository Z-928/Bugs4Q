from docplex.mp.model import Model
from qiskit.aqua.algorithms import VQE, ExactEigensolver
from qiskit.optimization.applications.ising import docplex

mdl = Model(name='wrong')
x = mdl.binary_var(name='x')
y = mdl.binary_var(name='y')
mdl.maximize(mdl.sum(x + y))
mdl.add_constraint(x == y)
print(mdl.export_to_string())

qubitOp, offset = docplex.get_qubitops(mdl)
print(qubitOp.print_details())
ee = ExactEigensolver(qubitOp, k=1)
result = ee.run()

sol = docplex.sample_most_likely(result['eigvecs'][0])
x = sol[0]
y = sol[1]
print('x', x)
print('y', y)
