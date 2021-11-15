from qiskit import *
qc = QuantumCircuit(2)
qc.initialize(0,0)
qc.initialize(1,1)

qc.h(0)
qc.h(1)
qc.cx(0,1)
qc.h(0)
qc.h(1)

qc.draw('mpl') 
usim = Aer.get_backend('unitary_simulator')
transpiled = transpile(qc, backend=usim)
transpiled.draw('mpl')
qobj = assemble(transpiled)
unitary = usim.run(qobj).result().get_unitary()
from qiskit.visualization import array_to_latex
array_to_latex(unitary, prefix="\\text{Circuit = }\n")