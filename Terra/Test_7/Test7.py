import qiskit as qk
qr = qk.QuantumRegister('qr', 1)
cr = qk.ClassicalRegister('cr', 1)
c = qk.QuantumCircuit(qr, cr)
c.x(qr)
c.measure(qr, cr)
qp = qk.QuantumProgram()
qp.add_circuit('test', c)



qobj = qp.compile('test', backend='local_qasm_simulator')
result = qp.run(qobj)    
   
# Following prints True
print(qobj['id'] == result._qobj['id'])

# Following prints True, False
print('result' in qobj,
      'result' in result._qobj)



qobj = qp.compile('test', backend='local_qasm_simulator')
result = qp.run(qobj)        
result = qp.run(qobj)

# Following prints True, True
print(qobj['id'] == result._qobj['id'], 
      qobj['id'] == result._qobj['result']._qobj['id'])

# Following prints True, True, False
print('result' in qobj, 
      'result' in result._qobj, 
      'result' in result._qobj['result']._qobj)
