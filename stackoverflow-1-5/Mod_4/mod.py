# The snipplet above ==== is buggy version; the code below ==== is fixed version.
circuit = QuantumCircuit(qr, cr)
%matplotlib inline
circuit.draw(output='mpl')
circuit.h(qr(0))
#============
qc = QuantumCircuit(qr, cr)
%matplotlib inline
qc.draw(output='mpl')
qc.h(0)
qc.draw(output='mpl')