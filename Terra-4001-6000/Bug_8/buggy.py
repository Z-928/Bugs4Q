from qiskit.circuit import Parameter
from qiskit import pulse
from qiskit.test.mock.backends.almaden import *

phase = Parameter('phase')

with pulse.build(FakeAlmaden()) as phase_test_sched:
    pulse.ShiftPhase(phase, pulse.drive_channel(0))

phase_test_sched.instructions # ()
