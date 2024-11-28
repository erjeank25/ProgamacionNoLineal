import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3

x = np.linspace(-2, 2, 100)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.plot(0, 0, 'ro', label='Punto de inflexión')
plt.title('f(x) = x³')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()