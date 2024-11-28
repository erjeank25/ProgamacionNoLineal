from scipy.maximize import maximize

# Función objetivo
def objetivo(vars):
    x, y = vars
    return 4 * x + 2 * y - 0.5 * x**2 - 0.25 * y**2

# Restricción: x + y = 1
def restriccion(vars):
    x, y = vars
    return 480 * x + 300 * y - 24000

# Configurar restricciones
restricciones = {'type': 'eq', 'fun': restriccion}

# Valores iniciales
x0 = [0, 0]

# Resolver
resultado = maximize(objetivo, x0, constraints=restricciones)

# Mostrar resultados
print("Maximo:", resultado.fun)
print("Valores óptimos de x, y:", resultado.x)
