import qiskit
from qiskit import available_backends, get_backend,\
    execute, QuantumRegister, ClassicalRegister, QuantumCircuit
import numpy as np

def round_to_zero(vec, tol=2e-15):
    vec.real[abs(vec.real) < tol] = 0.0
    vec.imag[abs(vec.imag) < tol] = 0.0
    return vec

def controlled(U):
    n = U.shape[0]
    return np.vstack((np.hstack((np.identity(n), np.zeros((n,n)))),
                      np.hstack((np.zeros((n,n)), U))))

def U(theta, phi, lam):
    return np.array([
        [np.cos(theta/2),
         -np.exp(1.j*lam)*np.sin(theta/2)],
        [np.exp(1.j*phi)*np.sin(theta/2),
         np.exp(1.j*(phi+lam))*np.cos(theta/2)]
    ])

Q_SPECS = {
    "name": "TestCU3",
    "circuits": [
        {
            "name": "TestCU3",
            "quantum_registers": [
                {
                    "name": "ctrl",
                    "size": 1
                },
                {
                    "name": "qb",
                    "size": 1
                },
            ],
            "classical_registers": []
        }
    ],
}
Q_program = qiskit.QuantumProgram(specs=Q_SPECS)

circuit = Q_program.get_circuit("TestCU3")
qb = Q_program.get_quantum_register("qb")
ctrl = Q_program.get_quantum_register("ctrl")

theta, phi, lam = np.pi, np.pi/2, 3*np.pi/2

circuit.cu3(theta, phi, lam, ctrl[0], qb[0])

unitary_sim = get_backend('local_unitary_simulator')
res = execute([circuit], unitary_sim).result()
unitary = round_to_zero(res.get_unitary())
wanted_unitary = round_to_zero(controlled(U(theta, phi, lam)))

print("Unitary matrix from simulator:\n", unitary, sep='')
print("Unitary matrix from theory:\n", wanted_unitary, sep='')
print("Unitary matrices are the same:", np.allclose(unitary, wanted_unitary))



###############################################################################################



from sympy import pi
def crzz(circuit, theta, ctrl, target):
    circuit.cu1(theta, ctrl, target)
    circuit.cx(ctrl, target)
    circuit.cu1(theta, ctrl, target)
    circuit.cx(ctrl, target)

def crx(circuit, theta, ctrl, target):
    # Apply the supposed c-RX operation.
    circuit.cu3(theta, pi/2, 3*pi/2, ctrl, target)
    # For the moment, QISKit adds a phase to the U-gate, so we
    # need to correct this phase with a controlled Rzz.
    crzz(circuit, pi, ctrl, target)
