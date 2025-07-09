import numpy as np
import matplotlib.pyplot as plt

x, y = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-2, 2, 20))

u = y
v = -x

magnitude = np.sqrt(u**2 + v**2)
u_norm = u / magnitude
v_norm = v / magnitude

plt.figure(figsize=(6, 6))
plt.quiver(x, y, u_norm, v_norm, color='teal', scale=25)  
plt.xlabel('x')
plt.ylabel('y')
plt.title('Campo vectorial: dx/dt = y, dy/dt = -x')
plt.grid(True)
plt.axis('equal')

import os
os.makedirs("plots", exist_ok=True)
plt.savefig("plots/campo_vectorial.png")
plt.show()