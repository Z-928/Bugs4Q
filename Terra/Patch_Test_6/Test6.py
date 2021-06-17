from qiskit import QuantumProgram
import Qconfig

qp = QuantumProgram()

qp.set_api(Qconfig.APItoken, Qconfig.config['url'])

qr = qp.create_quantum_register('qr', 16) #if i create only 1, the program doesn't run
cr = qp.create_classical_register('cr', 16)

qc = qp.create_circuit('qc', [qr], [cr])

def pad_QId(circuit,N,qr):
    for ii in range(N): 
        circuit.barrier(qr)
        circuit.iden(qr)
    return circuit  
  
qc.x(qr[0])
qc = pad_QId(qc, 1000, qr[0])
qc.measure(qr[0], cr[0])

result = qp.execute('qc', timeout = 1000, backend = 'ibmqx5', shots = 8192, max_credits = 5)
result.get_counts('qc')
