from qiskit import *
import numpy as np
import matplotlib.pyplot as plt
size = 4
#size = 13
q = QuantumRegister(size, name='q')
ckt = QuantumCircuit(q, name='ckt')
initial_state=np.zeros(2**size)
initial_state[size] = 1
ckt.initialize(initial_state)
ckt.draw(output='mpl')
plt.show() 
# if you set size to, say 13, you will encounter this bug