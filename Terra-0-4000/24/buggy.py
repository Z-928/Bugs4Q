from qiskit import *
circuit = QuantumCircuit(3)
circuit.cx(0, 2)

basis = ['u1', 'cx']  
coupling_map = CouplingMap([(0, 1), (1, 2)])
result = transpile(circuit,
                   optimization_level=1,
                   basis_gates=basis,
                   coupling_map=coupling_map,
                   seed_transpiler=42)
print(result)
