import numpy 
import qiskit as qc 
from qiskit import QuantumCircuit, execute, Aer
import matplotlib
from qiskit.visualization import plot_state_city

circ = qc.QuantumCircuit(3)

circ.h(0)
circ.cx(0,1)
circ.cx(0,2)
print(circ.draw())
backend = Aer.get_backend('statevector_simulator')
job = execute(circ, backend)
result = job.result()
outputstate = result.get_statevector(circ, decimals=3)
print(outputstate)
plot_state_city(outputstate)
