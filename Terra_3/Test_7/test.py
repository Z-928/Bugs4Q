from qiskit import QuantumCircuit
from qiskit.circuit.library import RZXGate
from qiskit.pulse import Schedule

qc_cal = QuantumCircuit(2)
qc_cal.rzx(0.5, 0, 1)
qc_cal.add_calibration(RZXGate, (0, 1), params=[0.5], schedule=Schedule())
print(qc_cal.calibrations)

qc = QuantumCircuit(2)
qc += qc_cal
print(qc.calibrations)