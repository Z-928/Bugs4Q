N = 5
shor = Shor()
qc = shor.construct_circuit(N)
trans_qc = transpile(qc, backend)