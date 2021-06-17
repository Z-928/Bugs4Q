from qiskit import *
q = QuantumRegister(3)
c = ClassicalRegister(3)
circ = QuantumCircuit(q, c)
circ.ccx(q[0], q[1], q[2])
print(circ.qasm())

result = execute(circ, 'local_qasm_simulator').result()
result.get_ran_qasm(circ.name)  # does not return an answer
