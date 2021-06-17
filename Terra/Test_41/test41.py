from qiskit.wrapper import load_qasm_string

qasm_string = """OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];

gate my_swap a,b {swap a,b;} 

my_swap q[0],q[1];
"""
circuit = load_qasm_string(qasm_string)
print(circuit.qasm())


#######################################################

from qiskit.wrapper import load_qasm_string

qasm_string = """OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];

swap q[0],q[1];
"""
circuit = load_qasm_string(qasm_string)
print(circuit.qasm())
