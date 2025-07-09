import matplotlib.pyplot as plt

def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

n = 20
fibo = fibonacci(n)
indices = list(range(n))

golden_ratio = []
for i in range(n):
    if i >= 2 and fibo[i - 2] != 0:
        golden_ratio.append(fibo[i - 1] / fibo[i - 2])
    else:
        golden_ratio.append(None)

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(indices, fibo, marker='o', color='purple')
plt.title('Sucesión de Fibonacci')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(indices[2:], golden_ratio[2:], marker='x', color='orange', label='Razón Fib(n)/Fib(n-1)')
plt.axhline(y=1.618, color='gray', linestyle='--', label='Razón áurea ≈ 1.618')
plt.title('Convergencia hacia la razón áurea')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('plots/fibonacci.png')
plt.show()
