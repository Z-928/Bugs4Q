from docplex.mp.model import Model

from qiskit import BasicAer
from qiskit.aqua.algorithms import QAOA, NumPyMinimumEigensolver
from qiskit.optimization.algorithms import CobylaOptimizer, MinimumEigenOptimizer
from qiskit.optimization.algorithms.admm_optimizer import ADMMParameters, ADMMOptimizer
from qiskit.optimization.problems import QuadraticProgram

# define COBYLA optimizer to handle convex continuous problems.
cobyla = CobylaOptimizer()

# define QAOA via the minimum eigen optimizer
qaoa = MinimumEigenOptimizer(QAOA(quantum_instance=BasicAer.get_backend('statevector_simulator')))

# exact QUBO solver as classical benchmark
exact = MinimumEigenOptimizer(NumPyMinimumEigensolver())  # to solve QUBOs

# construct model using docplex
mdl = Model('ex6')

v = mdl.integer_var(1, 8, name='v')
w = mdl.binary_var(name='w')
t = mdl.binary_var(name='t')
u = mdl.binary_var(name='u')

mdl.maximize(t + u + w + v)

# load quadratic program from docplex model
qp = QuadraticProgram()
qp.from_docplex(mdl)
print(qp.export_as_lp_string())

admm_params = ADMMParameters(
    rho_initial=1001,
    beta=1000,
    factor_c=900,
    maxiter=100,
    three_block=True, tol=8
)

# define QUBO optimizer
qubo_optimizer = qaoa

# define classical optimizer
convex_optimizer = cobyla
# convex_optimizer = cplex  # uncomment to use CPLEX instead

# initialize ADMM with quantum QUBO optimizer and classical convex optimizer
admm_q = ADMMOptimizer(params=admm_params,
                       qubo_optimizer=qubo_optimizer,
                       continuous_optimizer=convex_optimizer)

result_q = admm_q.solve(qp)
print("x={}".format(result_q.x))
print("fval={:.2f}".format(result_q.fval))
