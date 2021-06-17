from qiskit import IBMQ
from qiskit.providers.aer.noise.device import basic_device_noise_model

IBMQ.load_accounts()
device = IBMQ.get_backend('ibmq_poughkeepsie')
properties = device.properties()
noise_model = basic_device_noise_model(properties, thermal_relaxation=False)
