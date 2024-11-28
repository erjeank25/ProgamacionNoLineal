import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -x**2 + 4

x = np.linspace(-3, 3, 100)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.plot(0, 4, 'ro', label='Máximo global')
plt.title('f(x) = -x² + 4')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()