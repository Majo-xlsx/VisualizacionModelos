import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

beta = 0.3   
gamma = 0.1  

N = 1000
I0 = 1      
R0 = 0      
S0 = N - I0 - R0  

def modelo_sir(y, t, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

t = np.linspace(0, 160, 160)

y0 = [S0, I0, R0]

sol = odeint(modelo_sir, y0, t, args=(beta, gamma))
S, I, R = sol.T

plt.figure(figsize=(10, 6))
plt.plot(t, S, label='Susceptibles')
plt.plot(t, I, label='Infectados')
plt.plot(t, R, label='Recuperados')
plt.xlabel('Días')
plt.ylabel('Número de personas')
plt.title('Modelo SIR (Epidemiológico)')
plt.legend()
plt.grid(True)

import os
os.makedirs("plots", exist_ok=True)
plt.savefig("plots/modelo_sir.png")
plt.show()
