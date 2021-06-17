from qiskit import IBMQ
IBMQ.load_account()
provider = IBMQ.get_provider(group = 'open')
from qiskit.providers.aer.noise import NoiseModel

backend = provider.get_backend('ibmq_16_melbourne')
print("From config : ", backend.configuration().basis_gates)
print("From the noise model : ",NoiseModel.from_backend(backend).basis_gates)
