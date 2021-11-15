from qiskit import *
#Creating a quantum circuit with two qubits
qc=QuantumCircuit(2)

#Set the state of the first qubit to|0⟩ and set the state of the second qubit to|1⟩.
qc.initialize(0,0)
qc.initialize(0,0)
#or
#qc.reset(0)
#qc.reset(1)
#qc.x(1)

#Applying Hadamard to both qubits
qc.h(0)
qc.h(1)


#Applying CNOT operator, where the controller qubit is the first qubit and the target qubit is the second qubit
qc.cx(0,1)

#Applying Hadamard to both qubits
qc.h(0)
qc.h(1)

#display(qc.draw()) 
usim = Aer.get_backend('unitary_simulator')
qobj = assemble(qc)
unitary = usim.run(qobj).result().get_unitary()
array_to_latex(unitary, pretext="\\text{Circuit = }\n")