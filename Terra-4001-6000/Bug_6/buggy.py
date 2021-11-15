qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

new_qc = transpile(qc, system, basis_gates=['rz', 'sx', 'x', 'ecr'])
new_qc.draw()
