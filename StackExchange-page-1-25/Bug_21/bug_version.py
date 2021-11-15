from qiskit import *
from qiskit.quantum_info import Operator
from qiskit.compiler import transpile
#%matplotlib inline

u = Operator([[0, 0, 1, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 1, 0, 0, 0]])

qc = QuantumCircuit(3)
qc.unitary(u, [0,1,2], label='u')

result = transpile(qc, basis_gates=['h', 's', 't', 'cx'], optimization_level=3)
result.draw(output='mpl')