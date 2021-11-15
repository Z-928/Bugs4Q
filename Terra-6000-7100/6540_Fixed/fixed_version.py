from qiskit import QuantumCircuit
qc = QuantumCircuit(3)

outer_level = QuantumCircuit(2, name='outer')
inner_level = QuantumCircuit(2, name='inner')
inner_level.x(0)
outer_level.append(inner_level.to_gate(), [0,1])

qc.append(outer_level.control(), [0,1,2])