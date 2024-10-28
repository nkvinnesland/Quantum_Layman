from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

# Create a quantum circuit with 2 qubits and 2 classical bits
# Step 1: Apply Hadamard gates to put the qubits into superposition
# Step 2: Oracle for the marked state |11⟩ (example search target)
# Step 3: Apply Hadamard gates again
# Step 4: Grover Diffusion Operator (amplifying the marked state)
# Step 5: Measure the qubits
qc = QuantumCircuit(2, 2)
qc.h([0, 1])
qc.cz(0, 1)
qc.h([0, 1])
qc.z([0, 1])  # Z gates on both qubits
qc.cz(0, 1)   # Controlled-Z to entangle them
qc.h([0, 1])
qc.measure([0, 1], [0, 1])

# Simulate the quantum circuit
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit, shots=1024).result()

# Get the results and plot
counts = result.get_counts(qc)
print(counts)

# Draw the quantum circuit as a matplotlib plot
qc.draw(output='mpl')

# Print the quantum circuit to the console
print(qc.draw(output='text'))
