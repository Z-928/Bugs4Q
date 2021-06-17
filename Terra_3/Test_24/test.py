import qiskit as qk
# use the code in this file as commands
theta = qk.circuit.Parameter('theta')
qc = qk.QuantumCircuit(1)
qc.rx(theta, 0)
print(qc)

phi = qk.circuit.Parameter('phi')
qc.bind_parameters({phi: 0.1})

qc.bind_parameters({qk.circuit.Parameter('theta'): 0.1})

qc.bind_parameters({'theta': 0.1})
qc.bind_parameters({'theta': 0.1})
print(qc)

qc.bind_parameters({None: 0.1})
print(qc)

qc.assign_parameters({None: 0.1})
print(qc)