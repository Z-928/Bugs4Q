from qiskit import QuantumCircuit
from qiskit.transpiler import PassManager, CouplingMap
from qiskit.transpiler.passes import SabreSwap

from qiskit.test.mock.backends import FakeTenerife

coupling_map = CouplingMap(FakeTenerife().configuration().coupling_map)
print(coupling_map)

passmanager = PassManager(SabreSwap(coupling_map))
result = passmanager.run(QuantumCircuit(1))

print(coupling_map)