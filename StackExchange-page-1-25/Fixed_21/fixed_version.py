from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator
from qiskit.compiler import transpile

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

transpiled = transpile(qc, basis_gates=['u1', 'u2', 'u3', 'cx'], optimization_level=3)

from qiskit.circuit.library import TGate, HGate, SGate
from qiskit.transpiler.passes import SolovayKitaevDecomposition

basis_gates = [TGate(), SGate(), HGate()]
skd = SolovayKitaevDecomposition(recursion_degree=3, basis_gates=basis_gates, depth=5)
discretized = skd(transpiled)
print(discretized)