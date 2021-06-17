from qiskit import QuantumRegister
from qiskit import QuantumCircuit
from qiskit.circuit import Gate

q = QuantumRegister(3)
circ = QuantumCircuit(q)
my_gate = Gate(name='my_gate', num_qubits=2, params=[])
circ.append(my_gate, [q[0], q[1]])
circ.append(my_gate, [q[1], q[2]])
circ.draw()

#####################################################################################

# build a sub-circuit
sub_q = QuantumRegister(2)
sub_circ = QuantumCircuit(sub_q, name='sub_circ')
sub_circ.h(sub_q[0])
sub_circ.crz(0.1, sub_q[0], sub_q[1])
sub_circ.barrier()
sub_circ.iden(sub_q[1])
sub_circ.u3(0.1, 0.2, -0.2, sub_q[0])

# convert to a gate and stick it into an arbitrary place in the bigger circuit
sub_inst = sub_circ.to_instruction()
circ.append(sub_inst, [q[1], q[2]])
circ.draw()

#####################################################################################

from qiskit import BasicAer
from qiskit.transpiler.passes import Decompose
from qiskit.transpiler import PassManager, transpile

sim = BasicAer.get_backend('qasm_simulator')

passes = [
    Decompose()
]
pm = PassManager(passes)
new_circ = transpile(circ, sim, pass_manager=pm)
new_circ.draw()
