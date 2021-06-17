from qiskit import IBMQ
from qiskit.providers.aer.noise.device import models
import qiskit.quantum_info as qi

# Get backend properties
provider = IBMQ.load_account()
properties = provider.get_backend('ibmq_vigo').properties()

# Get device errors
errors_dr = models.basic_device_gate_errors(properties,
                                            gate_error=True,
                                            thermal_relaxation=True)

errors_r = models.basic_device_gate_errors(properties,
                                           gate_error=False,
                                           thermal_relaxation=True)

errors_d = models.basic_device_gate_errors(properties,
                                           gate_error=True,
                                           thermal_relaxation=False)

# Calculate infidelities of errors
print('Gate Infidelities (relax + depol, depol, relax)')
for tup_dr, tup_r, tup_d in zip(errors_dr, errors_d, errors_r):
    gate = tup_dr[0]
    qubits = tup_dr[1]
    infids = [round(qi.gate_error(tup[2]), 5)
              for tup in (tup_dr, tup_r, tup_d)]
    print('{}{} = {}'.format(gate, qubits, infids))
