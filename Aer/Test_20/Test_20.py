import qiskit
from qiskit.providers.aer.extensions.snapshot_expectation_value import *
import numpy as np

n = 25
circ = qiskit.QuantumCircuit(n, n)
circ.h(0)
for i in range(n-1):
    circ.cx(0, i+1)
circ.snapshot_expectation_value('hi', [[1, 'Z']], [0])

sim = qiskit.Aer.get_backend('qasm_simulator')
res = qiskit.execute(circ, sim, shots=100).result()

print(res)
