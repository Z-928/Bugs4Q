
qasm_string="""
OPENQASM 2.0;
include "qelib1.inc";
qreg q[1];
creg c[1];
t q[0];
"""
circuit = load_qasm_string(qasm_string, name='tmp', basis_gates='t')
print(circuit.qasm())
#########################################################################################
#result:
OPENQASM 2.0;
include "qelib1.inc";
qreg q[1];
creg c[1];
tdg q[0];
