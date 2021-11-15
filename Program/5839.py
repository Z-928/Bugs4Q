# https://github.com/Qiskit/qiskit-terra/issues/5839


from qiskit import QuantumCircuit,QuantumRegister, Aer, execute
from qiskit.compiler import transpile
from qiskit.quantum_info.states.measures import state_fidelity
from IPython.core.display import display

# Create circuit
circ = QuantumCircuit(3)
circ.x(0)
circ.cnot(0,1)
circ.snapshot('snap1', snapshot_type='statevector')
circ.snapshot('snap1', snapshot_type='density_matrix')
circ.cnot(0,2)
circ.snapshot('snap2', snapshot_type='statevector')
circ.snapshot('snap2', snapshot_type='density_matrix')
circ.cnot(1,2)
circ.snapshot('snap3', snapshot_type='statevector')
circ.snapshot('snap3', snapshot_type='density_matrix')
circ.measure_all()

transpiled_circ = transpile(circ, coupling_map=[[0,1],[1,0],[1,2],[2,1]],optimization_level=2)

display(circ.draw())
display(transpiled_circ.draw())

results = execute(circ,Aer.get_backend('qasm_simulator')).result()
statevector1 = results.data()['snapshots']['statevector']['snap1'][0]
statevector2 = results.data()['snapshots']['statevector']['snap2'][0]
statevector3 = results.data()['snapshots']['statevector']['snap2'][0]
density_matrix1 = results.data()['snapshots']['density_matrix']['snap1'][0]['value']
density_matrix2 = results.data()['snapshots']['density_matrix']['snap2'][0]['value']
density_matrix3 = results.data()['snapshots']['density_matrix']['snap3'][0]['value']

results = execute(transpiled_circ,Aer.get_backend('qasm_simulator')).result()
statevector_transpiled1 = results.data()['snapshots']['statevector']['snap1'][0]
statevector_transpiled2 = results.data()['snapshots']['statevector']['snap2'][0]
statevector_transpiled3 = results.data()['snapshots']['statevector']['snap3'][0]
density_matrix_transpiled1 = results.data()['snapshots']['density_matrix']['snap1'][0]['value']
density_matrix_transpiled2 = results.data()['snapshots']['density_matrix']['snap2'][0]['value']
density_matrix_transpiled3 = results.data()['snapshots']['density_matrix']['snap3'][0]['value']

print('Fidelity between transpiled and normal statevector snapshots')
print('snap 1',state_fidelity(statevector_transpiled1,statevector1))
print('snap 2',state_fidelity(statevector_transpiled2,statevector2))
print('snap 3',state_fidelity(statevector_transpiled3,statevector3))
print('\nFidelity between transpiled and normal density matrix snapshots')
print('snap 1',state_fidelity(density_matrix_transpiled1,density_matrix1))
print('snap 2',state_fidelity(density_matrix_transpiled2,density_matrix2))
print('snap 3',state_fidelity(density_matrix_transpiled3,density_matrix3))
print('Counts normal: ',results.get_counts(circ))
print('Counts transpiled: ',results.get_counts(transpiled_circ))
