from qiskit import QuantumCircuit

qc = QuantumCircuit(1,1)
qc.measure(0,0)
qc.remove_final_measurements()

assert len(qc.cregs)==0, "idle classical register not removed"
assert len(qc.clbits)==0, f"idle classical bits not removed: {qc.clbits}"