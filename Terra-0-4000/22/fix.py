from qiskit import QuantumRegister, QuantumCircuit
from qiskit.converters import dag_to_circuit, circuit_to_dag
from qiskit.circuit import ControlledGate
from qiskit.dagcircuit import DAGCircuit

qr = QuantumRegister(4, 'qr')
ghz_circuit = QuantumCircuit(3, name='ghz')
ghz_circuit.h(0)
ghz_circuit.cx(0, 1)
ghz_circuit.cx(1, 2)
ghz = ghz_circuit.to_gate()
cghz = ghz.control(1)
circuit = QuantumCircuit(qr)
circuit.append(cghz, [3, 1, 0, 2])

print(circuit)

dag = circuit_to_dag(circuit)
for node in dag.topological_op_nodes():
    if isinstance(node.op, ControlledGate):
        controlled_qubits = node.qargs[:node.op.num_ctrl_qubits]
        unctl_dag = DAGCircuit()
        for qreg in dag.qregs.values():
            unctl_dag.add_qreg(qreg)

        unctl_dag = DAGCircuit()
        for qreg in dag.qregs.values():
            unctl_dag.add_qreg(qreg)
        unctl_dag.apply_operation_back(node.op.base_gate,
                               qr[node.op.num_ctrl_qubits:],
                               node.op.params)
        print(dag_to_circuit(unctl_dag))
        dag.substitute_node_with_dag(node, unctl_dag)

print(dag_to_circuit(dag))


