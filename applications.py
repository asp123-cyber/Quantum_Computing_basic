from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def dense_code(message):
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.cx(0, 1)          # Alice holds q0, Bob holds q1.
    if message[0] == "1":
        circuit.x(0)
    if message[1] == "1":
        circuit.z(0)
    # Alice sends q0. Bob now holds both qubits and decodes.
    circuit.cx(0, 1)
    circuit.h(0)
    return circuit


for message in ("00", "01", "10", "11"):
    decoded = Statevector(dense_code(message))
    print(message, "->", dict(decoded.probabilities_dict(decimals=6)))
    assert round(decoded.probabilities()[int(message, 2)], 6) == 1

search = QuantumCircuit(2)
search.h([0, 1])             # Four equal amplitudes.
search.cz(0, 1)              # Oracle marks |11> with a minus sign.
print("After marking:", Statevector(search).data.round(3))

search.h([0, 1])
search.x([0, 1])
search.cz(0, 1)
search.x([0, 1])
search.h([0, 1])             # Diffusion, up to a global phase.
answer = Statevector(search)
print("Final probabilities:", answer.probabilities().round(3))
assert round(answer.probabilities()[3], 6) == 1
