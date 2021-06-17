from qiskit.pulse.transforms import inline_subroutines
from qiskit.circuit import Parameter
import qiskit.pulse as pulse
from qiskit.pulse import Drag, DriveChannel, Gaussian


amp = Parameter("amp")
d0_ = DriveChannel(Parameter('ch0'))
sigma = Parameter("σ")

with pulse.build(name="xp") as xp:
    pulse.play(Gaussian(160, amp, sigma), d0_)

with pulse.build(name="xp2") as xp2:
    with pulse.align_sequential():
        pulse.call(xp)
        
print(xp2)
print(inline_subroutines(xp2))