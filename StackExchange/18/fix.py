from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

iqft = QFT(3, inverse=True)  # get the IQFT
reversed_bits_QFT = iqft.reverse_bits()  # reverse bit order

circuit = QuantumCircuit(3)
circuit.compose(reversed_bits_QFT, inplace=True)  # append your QFT 
