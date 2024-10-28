import numpy as np
import matplotlib.pyplot as plt

# Set up the x-axis (space) and the potential barrier
x = np.linspace(-10, 10, 500)
V = np.piecewise(x, [x < -2, (-2 <= x) & (x <= 2), x > 2], [0, 10, 0])  # Potential barrier

# Create a Gaussian wavefunction to represent the particle
def gaussian(x, mu, sigma):
    return np.exp(-(x - mu)**2 / (2 * sigma**2))

# Simulate the wavefunction before and after the barrier
psi_incoming = gaussian(x, -5, 1)  # Before the barrier
psi_tunneled = gaussian(x, 5, 1) * np.exp(-2)  # After the barrier (with decay factor)

# Plot the potential barrier
plt.plot(x, V, label="Potential Barrier", color="black")

# Plot the incoming and tunneled wavefunctions
plt.plot(x, psi_incoming, label="Incoming Wavefunction", color="blue")
plt.plot(x, psi_tunneled, label="Tunneled Wavefunction", color="green", linestyle='dashed')

# Set the plot labels and title
plt.title("Quantum Tunneling: Wavefunction and Barrier")
plt.xlabel("Position (x)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
