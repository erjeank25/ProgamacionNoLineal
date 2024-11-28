import cvxpy as cp

# Variables
x1 = cp.Variable()
x2 = cp.Variable()

# Función objetivo
objetivo = cp.Maximize(4 * x1 + 2 * x2 - 0.5 * x1**2 - 0.25 *x2)

# Restricciones
restricciones = [480 * x1 + 300 * x2 <= 24000]

# Problema
problema = cp.Problem(objetivo, restricciones)
problema.solve()

# Resultados
print("MAXIMO:", problema.value)
print("Valores óptimos de x1, x2:", x1.value, x2.value)
