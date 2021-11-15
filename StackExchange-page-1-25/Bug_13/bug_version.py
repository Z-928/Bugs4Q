BACKEND='ibmq_vigo'
JOB_ID='60037fbf2159c338e734e663'
my_backend = provider.get_backend(BACKEND)
my_job = my_backend.retrieve_job(JOB_ID)
COUNTS = my_job.result().get_counts()