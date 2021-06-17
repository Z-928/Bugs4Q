import qiskit as qk
import qiskit.providers.aer.extensions
qc = qk.QuantumCircuit(2, 1)
qc.snapshot_probabilities(label='before', qubits=[0])
qc.rz(0, 0)
qc.cz(0, 1)
qc.h(0)
qc.snapshot_probabilities(label='after', qubits=[0])
print(qc.draw(output='text'))
bkd = qk.Aer.get_backend('qasm_simulator')
res = qk.execute(qc, backend=bkd, shots=1, backend_options={"method": "density_matrix_gpu"}).result()
res = res.results[0]
res.data.snapshots.probabilities
