import numpy as np
from qiskit import *

sim = Aer.get_backend("qasm_simulator")
n_params0 = 5
n_params1 = 10
parameterizations = [
    [[[0, 0], np.linspace(0, 2*np.pi, n_params0)]],
    [[[1, 2], np.linspace(0, 2*np.pi, n_params1)]]
]

qc1 = QuantumCircuit(1, 1)
qc1.ry(1, 0)
qc1.measure(0, 0)

qc2 = QuantumCircuit(2, 2)
qc2.h(1)
qc2.u1(1, 1)
qc2.h(1)
qc2.measure([0, 1], [0, 1])

qobj = assemble(transpile([qc1, qc2], basis_gates=['h', 'u3'],optimization_level=0),
               parameterizations=parameterizations)
result = sim.run(qobj).result()

print('Status: {}'.format(result.status))
print("Results for parameterized circuit 0:")
for j in range(n_params0):
    print(result.get_counts(j))

print("Results for parameterized circuit 0:")
for j in range(n_params0, n_params0 + n_params1):
    print(result.get_counts(j))
