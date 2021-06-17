from qiskit import QuantumCircuit
qasm = """
OPENQASM 2.0;
include "qelib1.inc";
qreg q[1];
qreg r[1];
creg c[1];
cz q, r;
barrier q, r;
x q;
y q;
measure q -> c;
z q;
if (c==1) z r;
"""
circ = QuantumCircuit.from_qasm_str(qasm)
circ.draw(output='mpl')
