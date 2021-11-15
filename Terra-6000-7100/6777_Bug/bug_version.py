from qiskit.circuit import QuantumCircuit, Parameter
from qiskit_nature.drivers.second_quantization import PySCFDriver
from qiskit_nature.problems.second_quantization import ElectronicStructureProblem
from qiskit_nature.converters.second_quantization import QubitConverter
from qiskit.algorithms.optimizers import COBYLA
from qiskit.algorithms import VQE
from qiskit_nature.mappers.second_quantization import ParityMapper
from qiskit_nature.drivers import UnitsType, Molecule
from qiskit.circuit.library import TwoLocal
from qiskit.aqua.algorithms import NumPyMinimumEigensolver, VQE

molecule = Molecule(geometry=[['H', [0., 0., 0.]],
                              ['H', [0., 0., 0.735]]],
                     charge=0, multiplicity=1)
driver = PySCFDriver(molecule = molecule, unit=UnitsType.ANGSTROM, basis='sto3g')

es_problem = ElectronicStructureProblem(driver)
second_q_op = es_problem.second_q_ops()
qubit_converter = QubitConverter(mapper = ParityMapper(), two_qubit_reduction=True)
qubit_op = qubit_converter.convert(second_q_op[0], num_particles=es_problem.num_particles)

optimizer = COBYLA(maxiter=10000)

theta = Parameter('theta')
var_form = QuantumCircuit(2)
var_form.rx(theta, 1)

# fails, no set_max_evals_grouped
algo = VQE(qubit_op, var_form, optimizer)