from qiskit import QuantumCircuit
from qiskit.circuit.quantumregister import QuantumRegister
from qiskit.circuit.classicalregister import ClassicalRegister
from qiskit import Aer, execute
from qiskit.providers.aer.backends import QasmSimulator

def apply_measurement(circ):
    c = ClassicalRegister(len(circ.qubits), 'c')
    meas = QuantumCircuit(circ.qregs[0], c)
    meas.barrier(circ.qubits)
    meas.measure(circ.qubits,c)
    qc = circ+meas
    return qc

qr = QuantumRegister(4)
circ = QuantumCircuit(qr)
for i in range(4):
    for j in range(i+1,4):
        circ.cx(i,j)

qc = apply_measurement(circ)
circuits = [qc for i in range(3)]
num_shots = int(1e6)

backend = Aer.get_backend('qasm_simulator')
backend_options = {'method': 'automatic','max_parallel_threads':1,'max_parallel_experiments':1,'max_parallel_shots':1}
noiseless_qasm_result = execute(circuits, backend, shots=num_shots, backend_options=backend_options).result()
print(noiseless_qasm_result)

backend = Aer.get_backend('qasm_simulator')
backend_options = {'method': 'automatic','max_parallel_threads':1,'max_parallel_experiments':3,'max_parallel_shots':1}
noiseless_qasm_result = execute(circuits, backend, shots=num_shots, backend_options=backend_options).result()
print(noiseless_qasm_result)
