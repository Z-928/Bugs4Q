from qiskit import *
from qiskit.visualization import *
from qiskit.quantum_info import *

sv = Statevector.from_label('10')
mycircuit = QuantumCircuit(2)
mycircuit.h(0)
mycircuit.cx(0,1)
new_sv = sv.evolve(mycircuit)
plot_state_qsphere(new_sv.data)
