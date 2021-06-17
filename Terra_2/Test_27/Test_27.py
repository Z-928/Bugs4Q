from qiskit import IBMQ
from qiskit.compiler import assemble
from qiskit.assembler import assemble_schedules
from qiskit.pulse import functional_pulse
from qiskit import pulse

IBMQ.load_accounts()
backend_name = 'ibmq_poughkeepsie'
backend = IBMQ.get_backend(backend_name)

device = pulse.DeviceSpecification.create_from(backend)

@functional_pulse
def simple_square_pulse(duration):
    return [1/10] * duration

rabi_pulse = simple_square_pulse(duration=30)

schedule = pulse.Schedule(name='Simple square pulse')

schedule.insert(0, rabi_pulse(device.q[0].drive))

assemble_schedules([schedule])
