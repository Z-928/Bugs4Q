from qiskit.circuit import Gate
from qiskit.circuit import QuantumCircuit

test_gate = Gate('test',num_qubits=1,params=[])
test_qasm = 'OPENQASM 2.0;\ninclude "qelib1.inc";\n\nqreg q[2];\ncreg cr[2];\ntest q[0];\n'

test_circ = QuantumCircuit.from_qasm_str(test_qasm)
