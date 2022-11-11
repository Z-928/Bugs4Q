import random
import numpy as np
import cirq

circuit= cirq.Circuit()
p = 0.2
q = 0.1
r = 0.3
alice, bob, charlie = cirq.LineQubit.range(1, 4)
rho_12 = circuit.append([cirq.H(alice), cirq.CNOT(alice, bob)]) 
#circuit.append([cirq.H(alice), cirq.CNOT(alice, bob)]) 
rho_23 = circuit.append([cirq.H(bob), cirq.CNOT(bob, charlie)]) 
rho_13 = circuit.append([cirq.H(alice), cirq.CNOT(alice, charlie)]) 
#circuit = rho_12 + rho_23 + rho_13
print(circuit)
