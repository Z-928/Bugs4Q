def statepreparation(circuit, angle, wire):
	circuit.ry(angle[6], 0)


	control1 = RYGate(angle[5]).control(1, ctrl_state='1')
	circuit.append(control1, [0, 1])
	circuit.barrier()

	control2 = RYGate(angle[4]).control(1, ctrl_state='0')
	circuit.append(control2, [0, 1])
	circuit.barrier()

	control3 = RYGate(angle[3]).control(2, ctrl_state='11')
	circuit.append(control3, [0, 1, 2])
	circuit.barrier()

	control4 = RYGate(angle[2]).control(2, ctrl_state='10')
	circuit.append(control4, [0, 1, 2])
	circuit.barrier()

	control5 = RYGate(angle[1]).control(2, ctrl_state='01')
	circuit.append(control5, [0, 1, 2])
	circuit.barrier()

	control6 = RYGate(angle[0]).control(2, ctrl_state='00')
	circuit.append(control6, [0, 1, 2])
	circuit.barrier()

	return circuit
angle = feature_train1[1]
q = QuantumRegister(3) # QuantumRegister define number of qubit.
c = ClassicalRegister(1) # this defines a classical bit for storing measurement results
circuit = QuantumCircuit(q,c)
circuit = statepreparation(circuit, angle, [0,1,2])

#circuit.measure(0, c)

circuit.draw('mpl')