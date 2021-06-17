from qiskit import QuantumCircuit, execute, transpile, assemble, Aer
from qiskit.transpiler import CouplingMap
from qiskit.visualization import plot_histogram
from qiskit.transpiler import passes
from qiskit.transpiler import PassManager

circ = QuantumCircuit().from_qasm_str(qasm)
backend = Aer.get_backend('qasm_simulator')
coupling_map = [[0, 1], [1, 0], [1, 2], [1, 3], [2, 1], [3, 1], [3, 4], [4, 3]]

stochastic = passes.StochasticSwap(CouplingMap(coupling_map), seed=0)
lookahead = passes.LookaheadSwap(CouplingMap(coupling_map))
basic = passes.BasicSwap(CouplingMap(coupling_map))

pm = PassManager(stochastic)
new_circ = pm.run(circ)

counts_cm = backend.run(assemble(new_circ,shots=10000)).result().get_counts()
counts_no_cm = backend.run(assemble(circ,shots=10000)).result().get_counts()

plot_histogram([counts_cm,counts_no_cm],legend=['coupling_map','no_coupling_map'])
