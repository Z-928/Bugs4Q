from qiskit import Aer, QuantumCircuit

from qiskit.opflow import CircuitSampler, StateFn, Z, Y, I
from qiskit.utils import QuantumInstance
from qiskit.opflow.expectations import PauliExpectation
state = QuantumCircuit(2)

state.h(1)
state.sdg(1)
state.cz(0, 1)
state.h(1)
print(state)

obs = (Z ^ I) - 1j * (Y ^ I)

exp_val = ~StateFn(obs) @ StateFn(state)

print(exp_val)

print('Eval ', exp_val.eval())  # = 0+1j
print('Qasm ', CircuitSampler(QuantumInstance(Aer.get_backend('qasm_simulator'), shots=100000)).convert(PauliExpectation().convert(exp_val).reduce()).eval())  # = 0 (up to shot noise)