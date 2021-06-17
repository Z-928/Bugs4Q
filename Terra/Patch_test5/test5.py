######### OpenQASM #####################
OPENQASM 2.0;
include "qelib1.inc";

opaque mygate q1, q2, q3;
qreg q[3];
creg c[2];

mygate q[0], q[1], q[2];

measure q[0] -> c[0];
measure q[1] -> c[1];

################### parsing code ##############

from sys import argv
from pathlib import Path

import matplotlib
matplotlib.use('TkAgg') # OSX workaround

from qiskit.qasm import Qasm
from qiskit.unroll import Unroller, CircuitBackend
from qiskit.tools.visualization import circuit_drawer

if len(argv) != 2:
    raise RuntimeError("Exactly 1 argument is required.")

print(f"Opening {argv[1]}")
path = Path(argv[1]).resolve(strict=True)
qasm = Qasm(filename=str(path)).parse()
circuit = Unroller(qasm, CircuitBackend(
    basis=["u1","u2","u3","id","cx","x","y","z","h","s","t","rx","ry","rz"])).execute()
im = circuit_drawer(circuit)
im.save(path.with_suffix('.png'))
