# Importing needed libraries
from qiskit import *
from qiskit.mapper import Layout
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Enable use of real device
IBMQ.load_accounts()
backend_exp = IBMQ.get_backend('ibmq_16_melbourne')

for u in range(0,1): # It isn't important, it is because I measured all qubit's T1
    u_st = str(u)
    file1 = 'T1__raw_qubit_' + u_st + '.txt'
    out1 = open( file1, 'w' )
    
    out1.write('# This is the qubit\'s ' + u_st +' T1 raw data \n' )
    
    circuit = []

    q = QuantumRegister(2, 'q') #Only changing this and the layout makes it works
    c1 = ClassicalRegister(1, 'c')
    qc = QuantumCircuit(q)
    mz = QuantumCircuit(q,c1)
    lay = Layout({ (q,0) : 0, (q,1):1 })

    # Exciting the qubit
    qc.x(q[0])
    qc.barrier(q)

    # Measurment on Z-axis
    mz.measure(q[0],c1[0])

    # Waiting time ( 30*0.12 us each iteration)
    for i in range(50):
        identity = QuantumCircuit(q,c1)
        identity.barrier(q)
        for k in range(i*30):
            identity.iden(q)
        identity.barrier(q)
        circuit.append(qc+identity+mz)

    # Running the experiment
    jobZ = execute(circuit, backend_exp, initial_layout=lay, shots=1024)
    
    out1.write('# N° id_gates Z-Measure Error \n')
    
    Result = jobZ.result() # Taking the results
    
    counts = []
    for i in range(50):
        counts.append(Result.get_counts(circuit[i]) )

    # Preparing the lists to make fits
    y = []
    x = []
    for i in range(50):
        py = counts[i]['1']/1024
        x.append(i*30*0.12)
        y.append( py )
        out1.write(str(i*30) + ' '+ str(py)  + '\n')       
    out1.write( '\n')
    
    def expo(x, amp, slope, high):
        y = amp*np.exp(-slope*x)+high
        return y

    x = np.array(x)
    y = np.array(y)
    err_y = np.array(err_y)
   

    params , paramscov = curve_fit(expo, x, y,p0=[1,0.02,0] )
    a =np.sqrt(np.diag(paramscov))
    out1.write('The raw T1 is ' + str(1/params[1])+ ' +- ' + str(a[1]/params[1]) + '\n')
    out1.close()
   
    
    plt.figure()
    plt.plot(x, expo(x, *params),
         label='Raw fitted function')
    plt.plot(x , y, 'ro', label= 'data')
    plt.xlabel( ' Time [us] ')
    plt.ylabel(' Probability of being in the excited state ')
    plt.legend()
    plt.savefig('plot_q_'+ u_st+ '_raw.png')
