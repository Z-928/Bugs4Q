qasm_string_1= """OPENQASM 2.0;
include "qelib1.inc";
qreg qr[2];
cx qr[0],qr[1];
rz(0.7) qr[1];
rx(1.570796) qr[1];
"""
qasm_string_2 = """OPENQASM 2.0;
include "qelib1.inc";
qreg qr[2];
y qr[0];
h qr[0];
s qr[0];
h qr[0];
"""

##########################################################

from qiskit import *
import Qconfig
from pprint import pprint
register(Qconfig.APItoken)
circ = load_qasm_string(qasm_string_1)
qobj = compile(circ, 'ibmqx4')
pprint(qobj)
