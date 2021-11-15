from qiskit import *

q = QuantumRegister(1) 
qc = QuantumCircuit(q) 
job = execute(qc, backend='local_statevector_simulator') 
job.result().get_data(qc).
