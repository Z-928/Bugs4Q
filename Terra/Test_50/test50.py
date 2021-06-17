from qiskit.wrapper import load_qasm_string
from qiskit.dagcircuit import DAGCircuit
from qiskit.transpiler import PassManager, transpile
from qiskit.transpiler._basepasses import TransformationPass

class BugPass(TransformationPass) :
    
    def run(self, dag):
        print("Activating")
        return DAGCircuit()

qasm = "OPENQASM 2.0;\ninclude \"qelib1.inc\";\nqreg q[2];\nh q[0];\ncx q[0],q[1];"
dag = DAGCircuit.fromQuantumCircuit(load_qasm_string(qasm))
pm = PassManager()
pm.add_passes(BugPass())

dag2 = transpile(dag,pass_manager=pm)

dag == dag2 # returns true but should be false
