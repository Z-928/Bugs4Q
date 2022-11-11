import cirq
import pytest

@pytest.mark.parametrize('n', [1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_decomposition_unitary(n):
    rs = np.random.RandomState(1234)
    diagonal_angles = [2 * np.pi * angle for angle in rs.rand(2 ** n)]
    diagonal_gate = cirq.DiagonalGate(diagonal_angles)
    decomposed_circ = cirq.Circuit(cirq.decompose(diagonal_gate(*cirq.LineQubit.range(n))))

    expected_f = [np.exp(1j * angle) for angle in diagonal_angles]
    assert cirq.is_unitary(np.diag(expected_f))
    assert cirq.is_diagonal(np.diag(expected_f))
    actual_unitary = cirq.unitary(decomposed_circ)
    cirq.testing.assert_allclose_up_to_global_phase(actual_unitary, np.diag(expected_f), rtol=1e-4, atol=1e-4)
    decomposed_f = actual_unitary.diagonal()

    np.testing.assert_allclose(decomposed_f, expected_f)
