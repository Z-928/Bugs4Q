from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import Aer, execute
import random

n = 8
gate_list = ['u1', 'u2', 'u3', 'id', 'x', 'y', 'z', 'h', 's'] 

selected_gates= []

for i in range(0,8):
  x = random.choice(gates)
  a = '({})'.format(i)
  k = x+a
  selected_gates.append(k)

print(selected_gates)
qr = QuantumCircuit(n)
qr.selected_gates[0]
qr.selected_gates[1]
qr.selected_gates[2]
qr.selected_gates[3]
qr.selected_gates[4]
qr.selected_gates[5]
qr.selected_gates[6]
qr.selected_gates[7]

qr.draw()
