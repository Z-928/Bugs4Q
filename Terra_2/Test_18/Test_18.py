import qiskit as qk
from qiskit.test.mock import FakeTenerife
qc = qk.QuantumCircuit(3,1)
qc.ccx(2,1,0).c_if(qc.cregs[0], 0)
qc.measure(2,0)
print(qc)
qk.transpile(qc, optimization_level=2,backend=FakeTenerife())
