from qiskit import *
import Qconfig
register(Qconfig.APItoken)
backend_5 = get_backend('ibmq_5_tenerife')
backend_16 = get_backend('ibmq_16_rueschlikon')
jobs_5 = backend_5.jobs(limit=10)
jobs_16 = backend_16.jobs(limit=10)

for job in jobs_5:
    print(job.id)

for job in jobs_16:
    print(job.id)
