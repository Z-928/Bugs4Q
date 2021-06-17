cmd_def = pulse.CmdDef.from_defaults(back_default.cmd_def, back_default.pulse_library)
system = pulse.PulseChannelSpec.from_backend(backend)
x90_qubit_param = # pulse parameters to update

calib.update_u_gates(x90_qubit_param, qubits=0, cmd_def=cmd_def, drives=system.drives)
cmd_def.get('u2', qubits=0, P0=0, P1=0).draw()