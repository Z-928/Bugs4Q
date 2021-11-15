from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit
from qiskit import IBMQ, execute
from qiskit.providers.ibmq import least_busy

provider = IBMQ.load_account()
memory_backends = provider.backends(filters=lambda b: b.configuration().memory)
backend = least_busy(memory_backends)
n = backend.configuration().n_qubits

qr = QuantumRegister(n)
cr = ClassicalRegister(n)
circuit = QuantumCircuit(qr, cr)
circuit.h(qr)
circuit.measure(qr,cr)

job = execute(circuit, backend, shots=2)
results = job.result().get_memory()

print(results)
