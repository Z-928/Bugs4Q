#change

qc = QuantumCircuit()
qc.from_qasm_str(qasm)

#to

qc = QuantumCircuit.from_qasm_str(qasm)
