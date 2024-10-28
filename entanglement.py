from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

# Create a quantum circuit with two qubits
qc = QuantumCircuit(2)

# Apply Hadamard gate to qubit 0 to create superposition
qc.h(0)

# Apply CNOT gate to entangle qubits 0 and 1
qc.cx(0, 1)

# Simulate and plot the Bloch sphere for the two-qubit system
simulator = Aer.get_backend('statevector_simulator')
result = simulator.run(transpile(qc, simulator)).result()
statevector = result.get_statevector()

# Plot the Bloch multivector (two-qubit Bloch sphere visualization)
plot_bloch_multivector(statevector)
plt.show()

# Draw the quantum circuit
qc.draw(output='mpl')
