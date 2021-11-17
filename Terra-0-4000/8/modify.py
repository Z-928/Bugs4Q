#change

job = execute(qc, backend='local_statevector_simulator') 
job.result().get_data(qc)

#to

qc.iden(q)
job = execute(qc, backend='local_statevector_simulator')
job.result().get_statevector()   # job.result().get_data(qc) also works
