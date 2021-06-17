from qiskit import *
from qiskit.providers.ibmq import least_busy
from qiskit.tools.visualization import plot_histogram

secret_number = '12'
secret_number = bin(int(secret_number)).replace('0b','')
len_secret = len(secret_number)
print('Your secret number as bytes:', secret_number)

circuit = QuantumCircuit(len_secret+1, len_secret)
_ar = [i for i in range(0, len_secret)]
circuit.h(_ar)
circuit.x(len_secret)
circuit.h(len_secret)
circuit.barrier()
for i in range(0, len_secret):
    if secret_number[i] == '1':
        circuit.cx(i, len_secret)
circuit.barrier()
circuit.h(_ar)
circuit.barrier()
circuit.measure(_ar, _ar)

IBMQ.load_account()
provider = IBMQ.get_provider('ibm-q')
qcomp = least_busy(provider.backends(simulator=False))

from qiskit.tools.monitor import job_monitor
job = execute(circuit, backend=qcomp, shots=1024)
job_monitor(job)
job_result = job.result()

from qiskit.ignis.mitigation.measurement import complete_meas_cal, CompleteMeasFitter
cal_circuits, state_labels = complete_meas_cal(qr=circuit.qregs[0], circlabel= 'measerrormittigationcal')
cal_job = execute(cal_circuits, backend=qcomp, shots=1024, optimization_level=0)
job_monitor(cal_job)
cal_results = cal_job.result()
meas_fitter = CompleteMeasFitter(cal_results, state_labels, circlabel= 'measerrormittigationcal')
meas_filter = meas_fitter.filter
mitigated_result = meas_filter.apply(job_result) # <= ERROR here - it is just {} instead of having values
job_counts = job_result.get_counts(circuit)
mitigated_counts = mitigated_result.get_counts(circuit)
plot_histogram([job_counts, mitigated_counts], legend=['device, noisy', 'device, mitigated'])
print(mitigated_result.get_counts(circuit))