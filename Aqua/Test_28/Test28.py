from qiskit.aqua.components import oracles

oracle = oracles.TruthTableOracle(bitmaps=["00000111"], mct_mode="noancilla")
print(oracle.circuit)
