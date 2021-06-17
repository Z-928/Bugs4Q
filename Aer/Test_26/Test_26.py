import numpy as np
from qiskit import Aer, execute, QuantumCircuit, ClassicalRegister, QuantumRegister
     
def qft(circ, q, n):
    """n-qubit QFT on q in circ."""
    for j in range(n):
        for k in range(j):
            circ.cu1(np.pi / float(2**(j - k)), q[j], q[k])
        circ.h(q[j])
     
#Takes in a circuit with an operator on qubit n and appends the qpe circuit
def x_qpe(circ, q, n):
    for i in range(n-1):
        circ.h(q[i])
    for j in range(0, n-1, 2): # Only place a CX^n on every other qubit, because CX^n = I for n even
        circ.cx(q[j], q[n-1])
    circ.barrier()
    qft(circ, q, n-1)
     
# build QPE circuit
n = 20
qr = QuantumRegister(n)
cr = ClassicalRegister(n)
x_qpe_qc = QuantumCircuit(qr, cr)
x_qpe_qc.rx(np.pi/2, qr[n-1])
x_qpe_qc.barrier()
x_qpe(x_qpe_qc, qr, n)
x_qpe_qc.barrier()
for i in range(n-1):
    x_qpe_qc.measure(qr[i], cr[i])
     
     
backend = Aer.get_backend("qasm_simulator")
p = 1
for i in range(1000):
    qobj = execute(x_qpe_qc, backend = backend, shots=1000)
    res = qobj.result()
    print("Finished {}th run".format(i))
