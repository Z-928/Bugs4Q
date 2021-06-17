from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.wrapper import execute as q_execute

import concurrent.futures
import multiprocessing as mp

def subrountine(depth):

	q = QuantumRegister(2, name='q')
	c = ClassicalRegister(2, name='c')
	qc = QuantumCircuit(q,c)

	qc.h(q[0])
	qc.h(q[1])
	for i in range(depth):
		qc.cx(q[0], q[1])
	qc.h(q[0])
	qc.h(q[1])


	qc.measure(q, c)
	ret = q_execute(qc, 'local_qasm_simulator', shots=100)
	ret = ret.result()
	return ret.get_counts()

if __name__ == '__main__':
	max_workers = min(2, mp.cpu_count())
	with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
		futures = [executor.submit(subrountine, depth) for depth in range(5)]
		for future in concurrent.futures.as_completed(futures):
			print(future.result())
      
####################################################comment#########################


from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.wrapper import execute as q_execute

def subrountine(depth):

    q = QuantumRegister(2, name='q')
    c = ClassicalRegister(2, name='c')
    qc = QuantumCircuit(q,c)
    qc.h(q[0])
    qc.h(q[1])
    for i in range(depth):
        qc.cx(q[0], q[1])
    qc.h(q[0])
    qc.h(q[1])
    qc.measure(q, c)
    ret = q_execute(qc, 'local_qasm_simulator', shots=1000)
    return ret

job_list = []
for depth in range(5):
    job_list.append(subrountine(depth))

jobs_not_done = list(range(5))
while jobs_not_done:
    for kk in jobs_not_done:
        if job_list[kk].status['status'].value == 'job has successfully run':
            jobs_not_done.remove(kk)
print('All jobs done, do processing here')
