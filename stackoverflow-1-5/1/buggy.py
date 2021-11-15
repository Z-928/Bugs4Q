from qiskit import *

qc = QuantumCircuit(3, 3)

qc.x(0) #q -> 1
qc.barrier()

qc.h(1)
qc.cx(1, 2)
qc.barrier()
# Next, apply the teleportation protocol.
qc.cx(0, 1)
qc.h(0)
qc.barrier()
# We measure these qubits and use the classical results to perform an operation
qc.measure(0, 0)
qc.measure(1, 1)
qc.cx(1, 2)
qc.cz(0, 2)
#qc.barrier()
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1, memory=True).result()
result = job.get_memory()[0]
qc.measure(2, 2)
print(job.get_memory()[0]) #q = 0
qc.draw()
