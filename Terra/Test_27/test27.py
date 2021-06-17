q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
circuit = QuantumCircuit(q, c)
circuit.h(q[0])
circuit.x(q[1])
circuit.cswap(q[0], q[1], q[2])
    
circuit.measure(q, c)
    
job = execute(circuit, 'local_qasm_simulator')
print(job.result().get_counts(circuit))
# {'010': 522, '111': 502}
