from qiskit import * 
qc = QuantumCircuit(1)
theta = qiskit.circuit.parameter('theta')
qc.rx(theta, 0)
qc,x(0)
qiskit.compiler.transpile(qc, optimization_level=3)
