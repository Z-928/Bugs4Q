from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, \
    Aer, BasicAer, execute

q = QuantumRegister(1, 'q')
c = ClassicalRegister(1, 'c')
o = ClassicalRegister(1, 'o')
C = QuantumCircuit(q, c, o)

C.x(q[0])
C.measure(q, o).c_if(c, 1)

print("BasicAer: {}".format(
    execute(C, BasicAer.get_backend('qasm_simulator'),
                                    shots=1 << 15).result().get_counts()))
print("Aer: {}".format(
    execute(C, Aer.get_backend('qasm_simulator'),
                               shots=1 << 15).result().get_counts()))
