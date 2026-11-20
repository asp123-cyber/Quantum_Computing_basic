from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

bell = QuantumCircuit(2)
bell.h(0)
bell.cx(0, 1)
print(bell.draw(output="text"))
print("Bell probabilities:", Statevector(bell).probabilities().round(3))

ghz = QuantumCircuit(3)
ghz.h(0)
ghz.cx(0, 1)
ghz.cx(1, 2)
state = Statevector(ghz)
state.seed(19)
print(ghz.draw(output="text"))
print("GHZ counts:", dict(state.sample_counts(100)))

kick = QuantumCircuit(2)
kick.h(0)                 # control in |+>
kick.x(1)
kick.h(1)                 # target in |->
kick.cx(0, 1)
kick.h(0)                 # read the control in the +/- basis
print("Control probabilities:", Statevector(kick).probabilities([0]).round(3))
