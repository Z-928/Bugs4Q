from qiskit.wrapper import load_qasm_string

qasm_string = """OPENQASM 2.0;
gate id a { U(0,0,0) a; }
"""
circuit = load_qasm_string(qasm_string)
print(circuit.definitions.keys())
