from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.wrapper import available_backends, get_backend
from qiskit.wrapper import execute as q_execute

q = QuantumRegister(2, name='q')
c = ClassicalRegister(2, name='c')
qc = QuantumCircuit(q,c)

qc.h(q[0])
qc.h(q[1])
qc.cx(q[0], q[1])
qc.measure(q, c)
z = 0.995004165 + 1j * 0.099833417
z = z / abs(z)
u_error = np.array([[1, 0], [0, z]])
noise_params = {'U':
                        {'gate_time': 1,
                        'p_depol': 0.001,
                        'p_pauli': [0, 0, 0.01],
                        'U_error': u_error
                        }
                    }
config = {"noise_params": noise_params}
ret = q_execute(qc, 'local_qasm_simulator_cpp', shots=1024, config=config)
ret = ret.result()
print(ret.get_counts())
