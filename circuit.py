from qiskit import QuantumCircuit

engine_circuit = QuantumCircuit(9)
engine_circuit.mct([0,2], 4)
engine_circuit.mct([1,2], 4)
engine_circuit.x(4)
engine_circuit.mct([0,4],5)
engine_circuit.x(5)
engine_circuit.mct([2,4,5],6)
engine_circuit.x(6)
engine_circuit.mct([3,4,5,6],7)
engine_circuit.x(7)
engine_circuit.mct([4,5,6,7],8);
engine_circuit.x([4,5,6,7])
engine_circuit.to_gate()
