# Quantum computing study notes

Start with [qubits and measurement](01_qubits_and_measurement.ipynb). Run the cells from the top, make a prediction, then change one gate and see what moves.

| Notebook | Question to work through | Plain Python version |
| --- | --- | --- |
| [1 · Qubits and measurement](01_qubits_and_measurement.ipynb) | How do amplitudes turn into shot counts? | [Original Bell-pair demo with Aer](intro.py) |
| [2 · Gate field notes](02_gate_field_notes.ipynb) | What does each common gate do to a chosen input? | [One wire](single_qubit_gates.py) · [Controls and swaps](multi_qubit_gates.py) |
| [3 · Building circuits](03_building_circuits.ipynb) | How do Bell pairs, GHZ states and phase kickback work? | [First circuits](first_circuits.py) |
| [4 · Small applications](04_small_applications.ipynb) | How can a circuit carry a message or find a marked answer? | [Applications](applications.py) |

## Run locally in VS Code

From the repository root, use PowerShell with Python 3.10 installed.

```powershell
cd Quantum_Computing
py -3.10 -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python single_qubit_gates.py
```

Open a notebook with the VS Code Jupyter extension. Choose **Select Kernel → Python Environments** and pick `Quantum_Computing\.venv`. Run All, then revisit the experiments individually. The examples run on a local simulator.

For a quick reference while experimenting, see IBM's [bit-ordering guide](https://quantum.cloud.ibm.com/docs/en/qiskit/bit-ordering) and [Statevector reference](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.quantum_info.Statevector).
