
#https://github.com/Qiskit/qiskit-terra/issues/2009



import numpy as np
from qiskit import *
from qiskit.tools.qi.qi import random_unitary_matrix
from qiskit.mapper import two_qubit_kak
q = QuantumRegister(2, 'q')
qc = QuantumCircuit(q)

num_gates = np.random.randint(30)
# h = 0, x = 1, y = 2, z = 3, cx = 4

for _ in range(num_gates):
    item = np.random.randint(5)
    if item in [0, 1, 2, 3]:
        idx = np.random.randint(size)
        if item == 0:
            qc.h(q[idx])
        elif item == 1:
            qc.x(q[idx])
        elif item == 2:
            qc.y(q[idx])
        elif item == 3:
            qc.z(q[idx])
    else:
        idx = np.random.permutation(size)
        qc.cx(q[int(idx[0])], q[int(idx[1])])
 
uni = Aer.get_backend('unitary_simulator')
res = execute(qc, uni).result()
U = res.get_unitary()
two_qubit_kak(U)
