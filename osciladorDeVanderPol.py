import numpy as np
import matplotlib.pyplot as plt
import os

mu = 1.5

x = np.linspace(-3, 3, 20)
y = np.linspace(-3, 3, 20)
X, Y = np.meshgrid(x, y)

U = Y
V = mu * (1 - X**2) * Y - X

norm = np.sqrt(U**2 + V**2)
U = U / norm
V = V / norm

plt.figure(figsize=(6, 6))
plt.quiver(X, Y, U, V, angles='xy', scale_units='xy')
plt.title('Campo vectorial: Van der Pol (μ = 1.5)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('equal')

os.makedirs("plots", exist_ok=True)
plt.savefig("plots/campo_vanderpol.png")
plt.show()