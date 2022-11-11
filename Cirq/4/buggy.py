import cirq

number =6
qubits = cirq.LineQubit.range(number) 
def n_party_GHZ_circuit(qubits)
      GHZ_circuit = cirq.Circuit(cirq.H(qubits[i]),
                           cirq.CNOT(qubits[i], qubits[j]))

GHZ = cirq.final_density_matrix(n_party_GHZ_circuit)
