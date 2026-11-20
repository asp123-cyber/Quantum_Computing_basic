from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)      # 2 qubits, 2 classical bits
qc.h(0)                        # put qubit 0 in superposition
qc.cx(0, 1)                    # entangle qubit 1 with qubit 0
qc.measure([0, 1], [0, 1])     # measure both

print(qc.draw())               # shows the circuit

sim = AerSimulator()
result = sim.run(transpile(qc, sim), shots=1000).result()
print(result.get_counts())

