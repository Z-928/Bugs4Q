from qiskit import Aer
import qiskit.aqua.operators as op


def evaluate_result(o):
    sampler = op.CircuitSampler(backend=Aer.get_backend('qasm_simulator'), statevector=False)
    sampled_op = sampler.convert(o)
    return sampled_op.eval().real


if __name__ == '__main__':
    v1 = evaluate_result(op.PauliExpectation().convert(op.OperatorStateFn(op.X).adjoint() @ op.VectorStateFn([1, 1], coeff=2)))
    v2 = evaluate_result(op.PauliExpectation().convert(op.OperatorStateFn(op.X).adjoint() @ op.DictStateFn({'0': 1, '1': 1}, coeff=2)))
    print(f"v1 = {v1}\nv2 = {v2}")
