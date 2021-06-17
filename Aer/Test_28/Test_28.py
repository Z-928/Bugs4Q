from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, Aer, execute

q = QuantumRegister(50)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)

qc.h(q[0])
qc.cx(q[0], q[1])
for kk in range(2,50):
    qc.t(q[kk])
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])
backend = Aer.get_backend('qasm_simulator')
job_sim = execute(qc, backend)
