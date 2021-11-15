import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import random

m, b = 1, 0

lower, upper = -40, 40
num_points = 80
x1 = [random.randrange(start=-40, stop=40) for i in range(num_points)]
x2 = [random.randrange(start=-40, stop=40) for i in range(num_points)]

y1 = [random.randrange(start=lower, stop=m*x+b) for x in x1]
y2 = [random.randrange(start=m*x+b, stop=upper) for x in x2]


plt.plot(np.arange(-40,40), m*np.arange(-40,40)+b)
plt.scatter(x1, y1, c='red')
plt.scatter(x2, y2, c='blue')
plt.show()

x1, x2, y1, y2 = np.array(x1).reshape(-1,1), np.array(x2).reshape(-1,1), np.array(y1).reshape(-1,1), np.array(y2).reshape(-1,1)

x_upper = np.concatenate((x2, y2), axis=1)
x_lower = np.concatenate((x1, y1), axis=1)

X = np.concatenate((x_upper, x_lower), axis=0)

res1 = np.array([-1]*len(x1))
res2 = np.array([1]*len(x2))

y = np.concatenate((res1, res2), axis=0)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)


import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import Aer
from qiskit import execute
import numpy as np
%matplotlib inline
backend_sim = Aer.get_backend('qasm_simulator')

def quant_state(x1, x2, backend_sim = backend_sim):
    x1 = x1
    x2  = x2
    r = x1 * x1 + x2 * x2
    a = np.sqrt(1 + 2*r)
    psi = [0, 0, 0.5, 0, 0, -0.5, 0, 0, 1/(np.sqrt(2)*a), 0, x1/(np.sqrt(2)*a), x2/(np.sqrt(2)*a), x1/(np.sqrt(2)*a), x2/(np.sqrt(2)*a), 0, 0]
    qc = QuantumCircuit(4)
    qc.initialize(psi, [0,1,2,3])
    qc.h(0)
    qc.measure_all()
    job_sim = execute(qc, backend_sim, shots=1000)
    result_sim = job_sim.result()
    counts = result_sim.get_counts(qc)

    quantumState_1 = 0
    for i in counts.keys():
        list_i = list(i)
        if list_i[len(list_i) - 1] == '1':
            quantumState_1 += counts[i]

    return quantumState_1

quant_res = []

for i,j in zip(X_test[:, 0], X_test[:, 1]):
    qs = quant_state(i, j, backend_sim = backend_sim)
    if qs >= 500:
        quant_res.append(1)
    else:
        quant_res.append(-1)

def get_color(y,zn):
    colors = []

    for i in range(len(y)):
        if y[i] == zn:
            colors.append('red')
        else:
            colors.append('blue')

    return(colors)

quantColors = get_color(quant_res, 1)
plt.scatter(X_train[:, 0], X_train[:, 1], c = colors)
plt.scatter(X_test[:, 0], X_test[:, 1], c = quantColors, marker = "x")
plt.plot(np.arange(-40,40), m*np.arange(-40,40)+b)
plt.show()