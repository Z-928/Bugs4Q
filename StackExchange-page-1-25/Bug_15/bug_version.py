from qiskit.circuit.library import TwoLocal
import numpy as np

    rot = TwoLocal(
        int(np.sum(num_qubits)),
        "ry",
        [],
        reps=1,
        skip_final_rotation_layer=True,
        parameter_prefix="p",
    )

    var = TwoLocal(
            int(np.sum(num_qubits)),
            "ry",
            "cx",
            entanglement="linear",
            reps=1,
            skip_final_rotation_layer=True,
        )
    rot.num_parameters_settable()
    >> 2
    rot.compose(var, inplace=True)
    rot.num_parameters_settable()
    >> 2