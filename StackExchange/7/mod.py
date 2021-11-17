#change
counts  = result.get_counts(circuit)
print(counts)


# to
backend = Aer.get_backend('statevector_simulator')
statevector = result.get_statevector(circuit)
print(statevector)
