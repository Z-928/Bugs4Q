from qiskit import *
from qiskit.circuit import Parameter
import sympy as sy
x=Parameter('x')
theta=Parameter('θ')
phase=sy.atan2(sy.N(x)*sy.sin(theta),sy.cos(theta))
circuit = QuantumCircuit(3,3)

circuit.cu1(phase,0,1)
