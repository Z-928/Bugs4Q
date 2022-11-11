import cirq
qubit = cirq.NamedQubit("myqubit")
circuit = cirq.Circuit()
circuit = cirq.Circuit(cirq.H(qubit))
circuit.append(cirq.measure(qubit, key='result'))
print(circuit)
s=cirq.Simulator()
samples=s.run(circuit, repetitions=1000)
print('Single measurement result:' ,samples.histogram(key='result'))

print('****************************************')
circuit2 = cirq.Circuit(cirq.H(qubit))
for i in range(10):
    circuit2.append(cirq.measure(qubit, key='myqubit'))
print(circuit2)
samples2 = s.run(circuit, repetitions=1000)
print('Hadamard follows by 10 measurements result:' ,samples2.histogram(key='result'))
