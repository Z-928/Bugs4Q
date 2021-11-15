backend = "ibmq_16_rueschlikon"
my_backend = get_backend(backend)
circuits = []
for i in range(2):
    qr = QuantumRegister(2)
    cr = ClassicalRegister(2)
    circuit = QuantumCircuit(qr,cr)
    circuit.h(qr[0])
    circuit.cx(qr[0], qr[1])
    circuit.measure(qr,cr)
    circuits.append(circuit)
    
job_exp = compile(circuits, backend=backend, shots=1024)
