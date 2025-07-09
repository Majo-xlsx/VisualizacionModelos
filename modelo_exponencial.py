import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 100)
y = np.exp(0.3 * t)

plt.figure(figsize=(8, 4))
plt.plot(t, y, label='y(t) = e^(0.3t)', color='royalblue')
plt.title('Modelo de crecimiento exponencial')
plt.xlabel('Tiempo (t)')
plt.ylabel('y(t)')
plt.grid(True)
plt.legend()
plt.savefig('modelo_exponencial.png') 
plt.show()
