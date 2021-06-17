import itertools
import numpy as np
import itertools
from functools import reduce, partial

from qiskit import Aer, QuantumRegister, ClassicalRegister, execute, QuantumCircuit
from qiskit.tools.visualization import circuit_drawer
from qiskit.quantum_info import Pauli
from qiskit.aqua import QuantumInstance
from qiskit.aqua.operators import WeightedPauliOperator
from qiskit.aqua.components.initial_states import Custom
from qiskit.aqua.components.optimizers import COBYLA
from qiskit.aqua.algorithms import QAOA

np.set_printoptions(precision=3, suppress=True)


n_qubits = 2
n_system = n_qubits * 2
T = 1000

weights = np.array([[0,1],[0,0]])
p = 2

def product_pauli_z(q1, q2, coeff):
    eye = np.eye((n_system))
    return WeightedPauliOperator([[coeff, Pauli(eye[q1], np.zeros(n_system)) * Pauli(eye[q2], np.zeros(n_system))]])

def ising_hamiltonian(weights):
    H = reduce(lambda x,y:x+y,
            [product_pauli_z(i,j, -weights[i,j])
             for (i,j) in itertools.product(range(n_qubits), range(n_qubits))])
    #H.to_matrix()
    return H

Hc = ising_hamiltonian(weights)
print(Hc.print_details())


qr = QuantumRegister(n_system)
cr = ClassicalRegister(n_system)
backend = Aer.get_backend('qasm_simulator')


def prepare_init_state(T):
    init_circuit = QuantumCircuit(qr)
    α = 2 * np.arctan(np.exp(- 1/T))
    for i in range(n_qubits):
        init_circuit.rx(α, qr[n_qubits+i])
        init_circuit.cx(qr[n_qubits+i], qr[i])
    init_state = Custom(n_system, circuit=init_circuit)
    return init_state

initial_state = prepare_init_state(T)
print(prepare_init_state(T).construct_circuit())

optimizer = COBYLA()
qaoa = QAOA(Hc, optimizer, 2, initial_state)

backend = Aer.get_backend('statevector_simulator')
quantum_instance = QuantumInstance(backend)
result = qaoa.run(quantum_instance)
