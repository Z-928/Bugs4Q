from qiskit import *
from math import pi 
backend = Aer.get_backend('qasm_simulator')
# create Quantum Register called "qr" with 4 qubits
qr = QuantumRegister(4, name="qr")
# create Quantum Register called "cr" with 4 qubits
cr = ClassicalRegister(4, name="cr")
# Creating Quantum Circuit called "qc" involving your Quantum Register "qr"
# and your Classical Register "cr"
qc = QuantumCircuit(qr, cr, name="solve_linear_sys")        

# Initialize times that we get the result vector 
n0 = 0
n1 = 0

for i in range(10):
    #Set the input|b> state"
    qc.x(qr[2])

    #Set the phase estimation circuit
    qc.h(qr[0])
    qc.h(qr[1]) 
    qc.u1(pi, qr[0])
    qc.u1(pi/2, qr[1])
    qc.cx(qr[1], qr[2])

    #The quantum inverse  Fourier transform 
    qc.h(qr[0])
    qc.cu1(-pi/2, qr[0], qr[1])
    qc.h(qr[1])

    #R（lamda^-1） Rotation
    qc.x(qr[1])
    qc.cu3(pi/16, 0, 0, qr[0], qr[3])
    qc.cu3(pi/8, 0, 0, qr[1], qr[3])   

    #Uncomputation
    qc.x(qr[1])
    qc.h(qr[1])
    qc.cu1(pi/2, qr[0], qr[1])
    qc.h(qr[0])

    qc.cx(qr[1], qr[2])
    qc.u1(-pi/2, qr[1])
    qc.u1(-pi, qr[0])

    qc.h(qr[1]) 
    qc.h(qr[0])

    # To measure the whole quantum register
    qc.measure(qr[0], cr[0])
    qc.measure(qr[1], cr[1])
    qc.measure(qr[2], cr[2])
    qc.measure(qr[3], cr[3])

    job = execute(qc, backend=backend, shots=8192,)
    result = job.result()

    # Get the sum og all results
    n0 = n0 + result.data("solve_linear_sys")['counts']['1000']
    n1 = n1 + result.data("solve_linear_sys")['counts']['1100']

    # print the result
    print(result)
#     print(result.get_data(qc))
    plot_histogram(result.get_counts())


#     Reset the circuit
    qc.reset(qr)

    # calculate the scale of the elements in result vectot and print it.
    p = n0/n1
    print(n0)
    print(n1)
    print(p)
