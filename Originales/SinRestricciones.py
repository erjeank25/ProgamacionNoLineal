from scipy.optimize import minimize

# Definimos la función objetivo
def objetivo(x):
    return x**2 + 4*x + 6

# Valor inicial
x0 = 0  # Punto de inicio

# Resolver
resultado = minimize(objetivo, x0)

# Mostrar resultados
print("Mínimo:", resultado.fun)
print("Valor óptimo de x:", resultado.x)
