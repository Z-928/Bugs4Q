#add

from qiskit.opflow.expectations import PauliExpectation

#change

print('Qasm ', CircuitSampler(QuantumInstance(Aer.get_backend('qasm_simulator'),
                               shots=100000)).convert(exp_val).eval())  # = 0 (up to shot noise)

#to

print('Qasm ', CircuitSampler(QuantumInstance(Aer.get_backend('qasm_simulator'),
                               shots=100000)).convert(PauliExpectation().convert(exp_val).reduce()).eval())  # = 0 (up to shot noise)
