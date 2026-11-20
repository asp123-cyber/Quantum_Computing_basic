from math import pi

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def show(name, gate, start="+"):
    circuit = QuantumCircuit(1)
    if start == "+":
        circuit.h(0)
    gate(circuit)
    state = Statevector.from_instruction(circuit)
    print(f"{name:12} on |{start}>   {state.data.round(3)}")


# Start in |0> so a flip is easy to see.
show("I", lambda q: q.id(0), "0")       # Leave the state alone.
show("X", lambda q: q.x(0), "0")        # Exchange |0> and |1>.
show("Y", lambda q: q.y(0), "0")        # |0> -> i|1>, |1> -> -i|0>.
show("H", lambda q: q.h(0), "0")        # Split the amplitude evenly.
show("SX", lambda q: q.sx(0), "0")      # Two SX gates make X.
show("SX dagger", lambda q: q.sxdg(0), "0")  # Undo SX.

# Start in |+> so both amplitudes are present. Watch the second one.
show("Z", lambda q: q.z(0))             # Change its sign.
show("S", lambda q: q.s(0))             # Multiply it by i.
show("S dagger", lambda q: q.sdg(0))    # Undo S.
show("T", lambda q: q.t(0))             # Add pi/4 of phase.
show("T dagger", lambda q: q.tdg(0))    # Undo T.
show("P(pi/3)", lambda q: q.p(pi/3, 0))  # Choose the phase angle.

# Angles are in radians. Try pi in place of pi/2.
show("RX(pi/2)", lambda q: q.rx(pi/2, 0), "0")
show("RY(pi/2)", lambda q: q.ry(pi/2, 0), "0")
show("RZ(pi/2)", lambda q: q.rz(pi/2, 0))
show("U", lambda q: q.u(pi/2, 0, pi, 0), "0")  # These angles give H.
