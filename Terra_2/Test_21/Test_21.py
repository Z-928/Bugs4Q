def construct_circuit(param, qr):
    qc = QuantumCircuit(qr)
    qc.ry(param, qr[0])
    return qc

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, BasicAer
from qiskit.circuit import Parameter
from qiskit.compiler import transpile, assemble
from qiskit.tools import parallel_map

num_processes = 4

qr = QuantumRegister(3)
cr = ClassicalRegister(3)

circuit = QuantumCircuit(qr, cr)
parameters = [Parameter('x{}'.format(i)) for i in range(num_processes)]


results = parallel_map(construct_circuit,
                               [(param) for param in parameters],
                               task_args=(qr,),
                               num_processes=num_processes)
        
for qc in results:
    circuit += qc
    
circuit = transpile(circuit)
backend = BasicAer.get_backend("qasm_simulator")
parameter_values = [{x: 1 for x in parameters}]

print(parameter_values)
qobj = assemble(circuit, backend=backend, parameter_binds=parameter_values)
