from qiskit import *
q = QuantumRegister(2)
c = ClassicalRegister(2)
circ = QuantumCircuit(q, c)
circ.h(q[0])
circ.cx(q[0], q[1])
circ.measure(q[0], c[0])

config = {
    'noise_params': {
        'U': {
            'U_error': [
                [[1, 0], [0, 0]],
                [[0, 0], [0.998, 0.002]]
                ]
            }
        }
    }

sim = 'local_qasm_simulator_cpp'
job = execute(circ, sim, config)
result = job.result()
result.get_counts()



#################################################################


from qiskit import *
q = QuantumRegister(2)
c = ClassicalRegister(2)
circ = QuantumCircuit(q, c)
circ.h(q[0])
circ.cx(q[0], q[1])
circ.measure(q[0], c[0])

config = {
    'noise_params': {
        'U': {
            'U_error': np.array([[1, 0], [0, np.exp(1j * 0.05)]])
            }
        }
    }

sim = 'local_qasm_simulator_cpp'
job = execute(circ, sim, config)
result = job.result()
result.get_counts()

######################################################################
q = QuantumRegister(2)
c = ClassicalRegister(2)
circ = QuantumCircuit(q, c)
circ.h(q[0])
circ.cx(q[0], q[1])
circ.measure(q[0], c[0])

config = {
    "shots": 1024,
    "max_threads_shot": 1,
    'max_threads_gate':1,
    'noise_params': {
        'U': {
            'U_error': np.array([[1, 0], [0, np.exp(1j * 0.05)]])
            }
        }
    }

sim = 'local_qasm_simulator_cpp'
job = execute(circ, sim, config)
result = job.result()
result.get_counts()
