from qiskit import *
qc = QuantumCircuit(3, 1) 
qc.reset(range(3))

qc.x(0)
qc.barrier()
qc.ccx(0, 1, 2) 
qc.barrier()
qc.measure(2, 0) 

backend = provider.get_backend('ibmq_athens')
qc_trans = transpile(qc, backend, initial_layout=[2,3,4], optimization_level=3)