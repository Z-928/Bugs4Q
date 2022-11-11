import cirq
qubit = cirq.NamedQubit("myqubit")
circuit = cirq.Circuit(cirq.H(qubit))
for i in range(10):
    result2 = cirq.measure(qubit, key='myqubit')
    print(result2)
print(circuit)
# run simulation
result = cirq.Simulator().simulate(circuit)
print("result:")
print(result)
print(result2)
