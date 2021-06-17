import qiskit.ignis.verification.quantum_volume as qv
qcs = qv.qv_circuits(qubit_lists=[[0,1]])
qc = qcs[0][0][0]
print(qc.qasm() + "\n")
new_qc = qc.from_qasm_str(qc.qasm())
