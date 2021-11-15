from qiskit.circuit import Parameter
from qiskit.circuit.library import RealAmplitudes
from qiskit.opflow import CircuitStateFn
from qiskit.opflow.gradients import Gradient

ansatz = RealAmplitudes(num_qubits=1, reps=1).decompose()
for method in ['param_shift', 'fin_diff', 'lin_comb']:
    grad = Gradient(method).convert(CircuitStateFn(ansatz))
    print(f"{method} is ok")