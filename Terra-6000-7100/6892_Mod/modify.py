#change

circuit.assign_parameters({x: 0.001}, inplace=True)

#to

bound_circuit = circuit.assign_parameters({x: 0.001}, inplace=False)
print(circuit.parameters)
print(circuit.global_phase)
