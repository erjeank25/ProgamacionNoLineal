import sympy as sp

# Definir las variables
x, y = sp.symbols('x y')

# Definir la función objetivo
f = 2*x**2 + 3*x*y + y**2 - 4*x - 6*y

# Calcular las derivadas parciales
f_x = sp.diff(f, x)
f_y = sp.diff(f, y)

# Resolver el sistema de ecuaciones
soluciones = sp.solve([f_x, f_y], [x, y])

# Mostrar las soluciones
print("Puntos críticos:", soluciones)
