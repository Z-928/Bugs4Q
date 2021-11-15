from qiskit import QuantumCircuit

qc = QuantumCircuit(3)
qc.cx(0, 1, ctrl_state='0')
qc.ccx(0, 1, 2, ctrl_state='00')
