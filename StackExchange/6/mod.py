#add
from qiskit.compiler import transpile, assemble


#change


backend = Aer.get_backend('qasm_simulator')
qobj_list = [compile(qc, backend) for qc in qc_list]
job_list = [backend.run(qobj) for qobj in qobj_list]

while job_list:
    for job in job_list:
        if job.status() in JOB_FINAL_STATES:
            job_list.remove(job)
            print(job.result().get_counts())
            
#to

backend = Aer.get_backend('qasm_simulator')
transpiled_circs = transpile(qc_list, backend=backend)
qobjs = assemble(transpiled_circs, backend=backend)
job_info = backend.run(qobjs)
for circ_index in range(len(transpiled_circs)):
    print(job_info.result().get_counts(transpiled_circs[circ_index]))
