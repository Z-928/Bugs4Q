from qiskit.circuit.library import HiddenLinearFunction
from qiskit.test.mock import FakeMontreal
from qiskit import transpile
circ = HiddenLinearFunction([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
circ.draw('mpl')
sc = transpile(circ, FakeMontreal(), scheduling_method='asap')
print(FakeMontreal().properties().gate_length('cx', (0, 1)) / FakeMontreal().configuration().dt) # 1728
print(FakeMontreal().properties().gate_length('cx', (1, 2)) / FakeMontreal().configuration().dt) # 2560