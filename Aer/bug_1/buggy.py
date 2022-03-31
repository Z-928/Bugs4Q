from qiskit import *

qr = QuantumRegister(5,'qr')
cr = ClassicalRegister(5, 'cr')
ghz = QuantumCircuit(qr, cr)

ghz.h(qr[0])
ghz.cx(qr[0],qr[1])
ghz.cx(qr[1],qr[2])
ghz.cx(qr[2],qr[3])
ghz.cx(qr[3],qr[4])
ghz.barrier(qr)
ghz.measure(qr,cr)
ghz.draw()

sim_backend = BasicAer.get_backend('statevector_simulator')
sim_result = execute(ghz, sim_backend).result()
print(sim_result.get_statevector(0))
