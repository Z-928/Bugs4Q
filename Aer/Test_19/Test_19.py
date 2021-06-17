from qiskit import execute
from qiskit import QuantumCircuit
from qiskit.test import mock
from qiskit.providers import aer
from qiskit.providers.aer.noise import NoiseModel

circ = QuantumCircuit(2)
circ.x(0)
circ.x(1)
circ.measure_all()

backend = mock.FakeSingapore()
noise_model = NoiseModel.from_backend(backend)
qobj = assemble(transpile(circ, backend), backend)
sim = aer.QasmSimulator()
sim.run(qobj, noise_model=noise_model).result()
