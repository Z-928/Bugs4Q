seed = 50
algorithm_globals.random_seed = seed
qi = QuantumInstance(Aer.get_backend('statevector_simulator'), seed_transpiler=seed, seed_simulator=seed)

ansatz = PauliTwoDesign(2, reps=1, seed=seed)

fidelity = QNSPSA.get_fidelity(ansatz)
my_opt = QNSPSA(fidelity, maxiter=1000)

vqe = VQE(ansatz, optimizer=my_opt, quantum_instance=qi)
result = vqe.compute_minimum_eigenvalue(operator=H2_op)
print(result)
optimizer_evals = result.optimizer_evals