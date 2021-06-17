from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute, Aer
import unittest


class TestStatevectorSimulator(unittest.TestCase):
    @staticmethod
    def get_bell_qc():
        qc = QuantumCircuit(name="Bell")

        q = QuantumRegister(2, "q")
        c = ClassicalRegister(2, "c")

        qc.add_register(q)
        qc.add_register(c)

        qc.h(q[0])
        qc.cx(q[0], q[1])
        qc.measure(q[0], c[0])
        qc.measure(q[1], c[1])
        return qc

    def test_bell_statevector(self):
        qc = TestStatevectorSimulator.get_bell_qc()
        shots = 10
        seed = 1    
        backend = Aer.get_backend("statevector_simulator")
        job = execute(qc, backend=backend, shots=shots, seed_simulator=seed)
        job_result = job.result()
        counts = job_result.get_counts(qc)
        print("Counts:",counts)
        self.assertEqual(len(counts),1)
        first_count = next(iter(counts.values()))
        self.assertEqual(first_count,1)

if __name__ == "__main__":
    unittest.main()
