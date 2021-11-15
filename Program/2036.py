# https://github.com/Qiskit/qiskit-terra/issues/2036


from qiskit import QuantumRegister, QuantumCircuit, ClassicalRegister, transpiler
import numpy as np

q = QuantumRegister(6, name='qn')
c = ClassicalRegister(2, name='cn')

zz = QuantumCircuit(q, c)
zz.h(q[0])
zz.h(q[5])
zz.cx(q[0], q[5])
zz.u1(2 * np.pi, q[5])
zz.cx(q[0], q[5])
zz.h(q[0])
zz.h(q[5])
zz.barrier(q)
zz.measure(q[0], c[0])
zz.measure(q[5], c[1])

print(zz)
new_zz = transpiler.transpile(zz, basis_gates='u1, u2, u3, cx, id',
                              coupling_map=[[0, 1], [0, 5], [1, 0], [1, 2], [2, 1], [2, 3],
                                            [3, 2], [3, 4], [4, 3], [4, 9], [5, 0], [5, 6],
                                            [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [7, 12],
                                            [8, 7], [8, 9], [9, 4], [9, 8], [9, 14], [10, 5],
                                            [10, 11], [10, 15], [11, 10], [11, 12], [12, 7],
                                            [12, 11], [12, 13], [13, 12], [13, 14], [14, 9],
                                            [14, 13], [14, 19], [15, 10], [15, 16], [16, 15],
                                            [16, 17], [17, 16], [17, 18], [18, 17], [18, 19],
                                            [19, 14], [19, 18]], initial_layout = {("qn", 0): ("q", 0), ("qn", 1): ("q", 1),
                          ("qn", 2): ("q", 2), ("qn", 3): ("q", 3), ("qn", 4): ("q", 4), ("qn", 5): ("q", 5)})

print(new_zz)
