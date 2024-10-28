from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1)

# Apply Hadamard gate to create superposition
qc.h(0)

# Simulate and plot the state on the Bloch sphere
simulator = Aer.get_backend('statevector_simulator')
result = simulator.run(transpile(qc, simulator)).result()
statevector = result.get_statevector()

# Plot the Bloch sphere
plot_bloch_multivector(statevector)
plt.show()

# Draw the quantum circuit
qc.draw(output='mpl')
