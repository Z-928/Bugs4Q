from qiskit import *
from qiskit.providers.aer import QasmSimulator

circuit = QuantumCircuit(2)
circuit.h(0)
circuit.h(1)
circuit.cx(0,1)
circuit.measure_all()

backend=QasmSimulator()
job_sim=backend.run(transpile(circuit,backend),shots=1024)
result_sim=job_sim.result()

counts=result_sim.get_counts(circuit)
print(counts)
print(circuit)
