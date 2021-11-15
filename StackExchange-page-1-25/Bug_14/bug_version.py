from qiskit.test.mock import FakeTokyo
from qiskit.circuit.measure import measure
from qiskit.execute_function import execute
from qiskit.circuit.quantumcircuit import QuantumCircuit
from qiskit.compiler import transpile

backend = FakeTokyo()

final_circuit = transpile(circuits=circuit,
                          backend=backend,
                          routing_method='sabre',
                          layout_method='sabre',
                          basis_gates=['u1', 'u2', 'u3', 'cx', 'id'])

final_circuit.barrier()
final_circuit.measure_all()

results = execute(final_circuit, backend).result()
counts = results.get_counts()
print("result : ", counts)