from qiskit import *
qr = QuantumRegister(2, name='qreg')
cr = ClassicalRegister(2, name='creg')
qc = QuantumCircuit(qr,cr)
qc.h(qr)
qc.measure_all()

bkd = Aer.get_backend('qasm_simulator')
res = execute(qc, backend = bkd).result()
print(res.get_counts())