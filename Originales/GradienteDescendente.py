import numpy as np

# Función objetivo y su derivada
def objetivo(x):
    return x**2 + 4*x + 6

def derivada(x):
    return 2*x + 4

# Parámetros del gradiente descendente
alpha = 0.1  # Tamaño del paso
x = 0  # Punto inicial
iteraciones = 100

# Gradiente descendente
for i in range(iteraciones):
    grad = derivada(x)
    x = x - alpha * grad
    if abs(grad) < 1e-6:  # Criterio de parada
        break

print("Mínimo:", objetivo(x))
print("Valor óptimo de x:", x)
