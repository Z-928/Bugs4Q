import cirq
number = 6
qubits = cirq.LineQubit.range(number) 
GHZ_circuit = cirq.Circuit(cirq.H(qubits[0]))
for i in range(number-1):
    C = cirq.Circuit(cirq.CX(qubits[i], qubits[i+1] ) )
    GHZ_circuit = GHZ_circuit + C                     

print(GHZ_circuit)
