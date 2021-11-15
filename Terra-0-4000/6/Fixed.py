from qiskit import QuantumCircuit,QuantumRegister,ClassicalRegister
from qiskit import *
from qiskit.providers.aer import QasmSimulator



#qp.set_api(Qconfig.APItoken, Qconfig.config['url'])

q = QuantumRegister(16) #if i create only 1, the program doesn't run
c = ClassicalRegister(16)

qc = QuantumCircuit(q, c)

def pad_QId(circuit,N,q):
    for ii in range(N): 
        circuit.barrier(q)
        circuit.id(q)
    return circuit  
  
qc.x(q[0])
qc = pad_QId(qc, 1000, q[0])
qc.measure(q[0], c[0])




result = execute(qc, timeout = 1000, backend=QasmSimulator(), shots = 8192, max_credits = 5)

counts = result.result().get_counts(qc)
print(counts)



