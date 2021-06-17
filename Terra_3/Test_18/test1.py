from qiskit import QuantumCircuit, IBMQ
from qiskit.compiler import transpile

IBMQ.load_account()
provider = IBMQ.get_provider(group = 'open')

backend = provider.get_backend('ibmq_16_melbourne')

qc = QuantumCircuit(5)
qc.h([0,2,3])
qc.i(0)
qc.cx(0,1)
qc.cx(2,1)
qc.cx(3,4)
qc.x([4,1])
qc.cz(2,0)
qc.cz(3,2)
qc.z([1,2,3])
qc.cx(0,3)
qc.cx(2,4)
qc.cx(3,0)
qc.measure_all()

trans = transpile(qc, backend, seed_transpiler = 2303, optimization_level = 2)
print("The depth of the transpiled circuit is : ", trans.depth())
print("Optim = 2 : ", trans.count_ops())