from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a quantum circuit with 3 qubits and 2 classical bits
qc = QuantumCircuit(3, 2)

# Step 1: Prepare qubit 0 in the |00> state (qubit 0 already initialized to |0⟩)
# No need to apply any gates to qubit 0, since it's already in |0⟩.

# Step 2: Entangle qubit 1 and qubit 2
qc.h(1)  # Hadamard gate on qubit 1 puts it into superposition
qc.cx(1, 2)  # CNOT gate entangles qubit 1 and qubit 2

# Add a barrier to ensure proper execution order
qc.barrier()

# Step 3: Bell measurement on qubit 0 and qubit 1 to teleport |00⟩
qc.cx(0, 1)  # CNOT gate for Bell measurement
qc.h(0)  # Hadamard gate on qubit 0 completes the Bell measurement
qc.measure([0, 1], [0, 1])  # Measure qubits 0 and 1, store results in classical bits

# Simulate the quantum circuit to get the classical measurement result
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit, shots=1).result()

# Get the classical measurement result
counts = result.get_counts()

# Extract the result (since we only have one shot, there will be only one result)
outcome = list(counts.keys())[0]
classical_bit_0 = outcome[1]  # Bit from qubit 0 measurement
classical_bit_1 = outcome[0]  # Bit from qubit 1 measurement

# Now we apply corrections based on the measurement results in Python logic
# If classical bit 1 == '1', apply X gate to qubit 2
if classical_bit_1 == '1':
    qc.x(2)
# If classical bit 0 == '1', apply Z gate to qubit 2
if classical_bit_0 == '1':
    qc.z(2)

# Add a final measurement for qubit 2 to verify the teleportation result
qc.measure(2, 0)

# Simulate again after applying the corrections
compiled_circuit_with_corrections = transpile(qc, simulator)
result_with_corrections = simulator.run(compiled_circuit_with_corrections, shots=5000).result()
counts_with_corrections = result_with_corrections.get_counts()

# Print results
print("\nResults after teleporting |00⟩ with corrections applied:")
print(counts_with_corrections)
plot_histogram(counts_with_corrections)
plt.show()

# Print the final quantum circuit
print("Final Quantum Circuit:")
print(qc.draw(output='text'))
