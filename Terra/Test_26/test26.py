from qiskit import CompositeGate, QuantumCircuit, QuantumRegister
from qiskit.extensions.standard.u1 import U1Gate

q = QuantumRegister(2)
composite_gate = CompositeGate("second_order_expansion", [], [q[i] for i in range(2)])
composite_gate._attach(U1Gate(0, q[0]))
qc1 = QuantumCircuit(q)
qc1._attach(composite_gate)
qc2 = QuantumCircuit(q)
qc2 = qc2 + qc1
