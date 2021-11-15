from qiskit.circuit.library import ZZFeatureMap
zz = ZZFeatureMap(2, entanglement="full", reps=2)
zz.draw("mpl")