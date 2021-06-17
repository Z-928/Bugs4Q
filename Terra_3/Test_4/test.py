from qiskit import QuantumCircuit
from qiskit.circuit.library import RZXGate
from qiskit.pulse import Schedule
from qiskit import *

qc_cal = QuantumCircuit(2)
qc_cal.rzx(0.5, 0, 1)
qc_cal.add_calibration(RZXGate, (0, 1), params=[0.5], schedule=Schedule())

qc_cal = transpile(qc_cal, backend)
print(qc_cal.calibrations)

qc = QuantumCircuit(2)
qc.h(0)

new_circ_cal_on_lhs = qc_cal + qc
print(new_circ_cal_on_lhs.calibrations) #calibration information is lost

new_circ_cal_on_rhs = qc +qc_cal
print(new_circ_cal_on_rhs.calibrations) #calibration information is kept