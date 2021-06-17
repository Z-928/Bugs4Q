from qiskit.converters import circuit_to_dag, dag_to_circuit
from qiskit.pulse import Schedule
from qiskit import QuantumCircuit
from qiskit.circuit.gate import Gate

empty_circuit = QuantumCircuit(1)

dummy_gate = Gate("my_dummy_gate", 1, [])
circuit_with_calibrated_pulse_definition = QuantumCircuit(1)
circuit_with_calibrated_pulse_definition.append(dummy_gate, qargs=[0])
circuit_with_calibrated_pulse_definition.add_calibration(dummy_gate, [0], Schedule())

empty_dag = circuit_to_dag(empty_circuit)
calibrated_dag = circuit_to_dag(circuit_with_calibrated_pulse_definition)
composed_dag = empty_dag.compose(calibrated_dag, inplace=False)

print("Empty DAG:     ", empty_dag.calibrations)
print("Calibrated DAG:", calibrated_dag.calibrations)
print("Composed DAG:  ", composed_dag.calibrations) # Should be the same as calibrated_dag