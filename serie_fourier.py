import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 1000)
y = np.zeros_like(x)

N = 3
for n in range(1, 2*N, 2):  # 1, 3, 5
    y += (4 / (np.pi * n)) * np.sin(n * x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label='Aproximación de onda cuadrada (N=3)', color='blue')
plt.title('Serie de Fourier - Onda Cuadrada')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('plots/serie_fourier.png')
plt.show()
