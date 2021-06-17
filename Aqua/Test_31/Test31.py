from qiskit.aqua.components.variational_forms import RYRZ
from qiskit.aqua.components.initial_states import Custom, Zero
import numpy as np
from qiskit import Aer, execute
#%matplotlib inline
custom = Custom(3, 'uniform')
ryrz = RYRZ(3, 1, entanglement='linear', initial_state=custom)
qc = ryrz.construct_circuit(np.zeros(ryrz.num_parameters))
print(len(qc.qasm())
for _ in range(3):    
    qc = ryrz.construct_circuit(np.zeros(ryrz.num_parameters))
    print(len(qc.qasm()))
    
    