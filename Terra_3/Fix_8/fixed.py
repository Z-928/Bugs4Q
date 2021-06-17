from qiskit.circuit.measure import measure
q = QuantumRegister(4)
c = ClassicalRegister(1)
// circuit = QuantumCircuit(q,c)
ang = feature_train[3]
circuit = statepreparation(ang, circuit, [0,1,2,3])
circuit.measure(0, 0)