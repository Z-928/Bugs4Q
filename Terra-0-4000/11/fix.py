from qiskit import *


qasm = '''OPENQASM 2.0;
include "qelib1.inc";
qreg q[1];
creg c[1];
measure q -> c;'''
qc = QuantumCircuit.from_qasm_str(qasm)

print( qc.qasm() )
