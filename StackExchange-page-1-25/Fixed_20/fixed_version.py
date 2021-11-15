import numpy as np
# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, transpile, Aer, IBMQ
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from ibm_quantum_widgets import *
from math import sqrt
from qiskit.quantum_info import DensityMatrix
from qiskit.circuit.library import QFT

# Loading your IBM Q account(s)
provider = IBMQ.load_account()

qc = QuantumCircuit(1,1)

init = [sqrt(3/4),-sqrt(1/4)]
qc.initialize(init,0)
qc.h(0)
qc.x(0)
qc.h(0)
qc = qc + QFT(1)

qc.draw()


s0 = DensityMatrix(qc)
sim = Aer.get_backend('unitary_simulator')
job = transpile(qc,sim)
state = sim.run(job).result().get_unitary()
print(qc.qasm())