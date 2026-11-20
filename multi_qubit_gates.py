from math import pi

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def mapping(label, gate):
    circuit = QuantumCircuit(len(label))
    gate(circuit)
    result = Statevector.from_label(label).evolve(circuit)
    return {str(k): complex(v) for k, v in result.to_dict().items()}


for label in ("00", "01", "10", "11"):
    print(label, "CX", mapping(label, lambda q: q.cx(0, 1)),
          "CZ", mapping(label, lambda q: q.cz(0, 1)),
          "SWAP", mapping(label, lambda q: q.swap(0, 1)))

print("CY:", mapping("01", lambda q: q.cy(0, 1)))
print("CH:", mapping("01", lambda q: q.ch(0, 1)))
print("Controlled phase:", mapping("11", lambda q: q.cp(pi/2, 0, 1)))
print("Toffoli:", mapping("011", lambda q: q.ccx(0, 1, 2)))
print("Fredkin:", mapping("011", lambda q: q.cswap(0, 1, 2)))
