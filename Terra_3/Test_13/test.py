import qiskit.pulse as qp
import numpy as np

chan = qp.DriveChannel(0)
with qp.build() as sched:
    qp.delay(np.int32(5), chan)
    qp.play(qp.library.Constant(50, 1.0), chan)