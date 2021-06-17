import qiskit.pulse as pulse
import qiskit.pulse.pulse_lib as pulse_lib
sched = pulse.Schedule()
sched += pulse_lib.square(1000, 1.0)(pulse.DriveChannel(0))
sched += pulse_lib.square(10, 1.0)(pulse.DriveChannel(1))
sched.draw(channels_to_plot=[pulse.DriveChannel(1)])
