import qiskit
qreg = qiskit.QuantumRegister(1, name="old")
circuit = qiskit.QuantumCircuit(qreg)
circuit.h(qreg)

#print(circuit)
#        ┌───┐
# old_0: ┤ H ├
#        └───┘

circuit.transform_registers(new_qregs=[qiskit.QuantumRegister(1, name="new")])

#print(circuit)
#        ┌───┐
# new_0: ┤ H ├
#        └───┘

print(circuit.qubits)
# [Qubit(QuantumRegister(1, 'new'), 0)]

print(circuit.qregs)
# [QuantumRegister(1, 'new')]