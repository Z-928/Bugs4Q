from qiskit import QuantumCircuit, QuantumRegister, QiskitError
from qiskit.compiler import transpile
from qiskit.transpiler import CouplingMap
q = QuantumRegister(2)
qc = QuantumCircuit(q)
qc.cx(q[0], q[1])
qc.cx(q[0], q[1])
coupling = CouplingMap([[0, 1]])
compiled = transpile(qc, coupling_map=CouplingMap([[0, 1]]), optimization_level=3)
print(compiled)
