from qiskit.quantum_info import SuperOp
from qiskit.providers.aer.noise import depolarizing_error, thermal_relaxation_error

depol = depolarizing_error(0.001, 1)
kraus = thermal_relaxation_error(50e3, 100e3, 100)

target = SuperOp(depol).compose(SuperOp(kraus))
actual = SuperOp(depol.compose(kraus))

print('Target:\n', target.data.round(3))
print('Actual:\n', actual.data.round(3))
