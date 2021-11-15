from qiskit import IBMQ
from qiskit.pulse import CmdDef
IBMQ.load_accounts()
backend = IBMQ.get_backend('ibmq_poughkeepsie')

default = backend.defaults()
cmd_def = CmdDef.from_defaults(default.cmd_def,default.pulse_library)
print(cmd_def.get_parameters('u3', 0))
cmd_def.get('u3', 0, 1, 2, 3)
