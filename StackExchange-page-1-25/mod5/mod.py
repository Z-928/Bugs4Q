#add
from qiskit.quantum_info import Statevector

#change
q1.save_statevector() 
q1.save_statevector() 
q1.save_statevector()

# to

st0 = Statevector.from_instruction(qc)
st1 = Statevector.from_instruction(qc)
st2 = Statevector.from_instruction(qc)
