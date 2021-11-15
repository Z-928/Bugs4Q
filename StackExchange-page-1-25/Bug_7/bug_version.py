from qiskit import *
import numpy as np

#Operator Imports
from qiskit.opflow import Z, X, I

#Circuit imports
from qiskit_nature.drivers import PySCFDriver, UnitsType, QMolecule, FermionicDriver
from qiskit_nature.problems.second_quantization.electronic import ElectronicStructureProblem
from qiskit_nature.circuit.library import HartreeFock, UCCSD, UCC
from qiskit_nature.transformers import FreezeCoreTransformer, ActiveSpaceTransformer
from qiskit_nature.algorithms import GroundStateEigensolver
from qiskit_nature.results import EigenstateResult
from qiskit import Aer
from qiskit_nature.mappers.second_quantization import ParityMapper, JordanWignerMapper
from qiskit_nature.converters.second_quantization import QubitConverter
from qiskit.algorithms.optimizers import L_BFGS_B, SPSA, AQGD, CG, ADAM, P_BFGS, SLSQP, NELDER_MEAD
from qiskit.algorithms import VQE, NumPyMinimumEigensolver
from qiskit.circuit.library import TwoLocal, EfficientSU2
import matplotlib.pyplot as plt
import matplotlib
from qiskit.tools.visualization import circuit_drawer
matplotlib.use('Agg')


driver = PySCFDriver(atom='H -1.9767, .0, 1.53054; \
                        O  .0, .0, .0; \
                        H 1.9767, .0, 1.53054;',
                     unit=UnitsType.ANGSTROM,
                     basis='sto3g')

at = ActiveSpaceTransformer(8, 5)
ft = FreezeCoreTransformer()

problem = ElectronicStructureProblem(driver, q_molecule_transformers=[ft, at])

# generate the second-quantized operators
second_q_ops = problem.second_q_ops()
main_op = second_q_ops[0]

num_particles = (problem.molecule_data_transformed.num_alpha,
                 problem.molecule_data_transformed.num_beta)

num_spin_orbitals = 2 * problem.molecule_data.num_molecular_orbitals
mapper = JordanWignerMapper()
converter = QubitConverter(mapper=mapper, two_qubit_reduction=True)
qubit_op = converter.convert(main_op, num_particles=num_particles)
init_state = HartreeFock(num_spin_orbitals, num_particles, converter)
# print(main_op)

def custom_excitation_list(num_spin_orbitals, num_particles):
   my_excitation_list = [((0, 2, 4, 6), (0 ,2, 4, 7), (0,2,5,6))]

   return my_excitation_list

circ = UCC(qubit_converter=converter, num_particles=num_particles, num_spin_orbitals=num_spin_orbitals, excitations=custom_excitation_list,  reps=1, initial_state=init_state)

print(circ.parameters)