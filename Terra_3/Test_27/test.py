from qiskit.pulse.transforms import inline_subroutines
from qiskit.circuit import Parameter
import qiskit.pulse as pulse
from qiskit.pulse import Drag, DriveChannel, Gaussian, ControlChannel, GaussianSquare

amp_cr = Parameter("amp")
amp = Parameter("amp")
d0 = DriveChannel(Parameter("ch0"))
c1 = ControlChannel(Parameter("ch0.1"))
sigma = Parameter("σ")
width = Parameter("w")
dur1 = Parameter("duration")
dur2 = Parameter("duration")

with pulse.build(name="xp") as xp:
    pulse.play(Gaussian(dur1, amp, sigma), d0)

with pulse.build(name="cr") as cr:
    with pulse.align_sequential():
            pulse.play(GaussianSquare(dur2, amp_cr, sigma, width), c1)
            pulse.call(xp)
            pulse.play(GaussianSquare(dur2, amp_cr, sigma, width), c1)
            pulse.call(xp)