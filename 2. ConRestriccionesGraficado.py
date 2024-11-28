from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

def parse_expression(expr_str):
    x, y, z = sp.symbols('x y z')
    return sp.sympify(expr_str)

def create_function(expr):
    x, y, z = sp.symbols('x y z')
    return sp.lambdify([x, y, z], expr, 'numpy')

def objetivo(vars):
    return obj_func(*vars)

def restriccion(vars):
    return const_func(*vars)

# Solicitar función objetivo
obj_str = input("Ingrese la función objetivo (use x, y, z como variables): ")
obj_expr = parse_expression(obj_str)
obj_func = create_function(obj_expr)

# Solicitar restricción
const_str = input("Ingrese la restricción (use x, y, z, igualada a 0): ")
const_expr = parse_expression(const_str)
const_func = create_function(const_expr)

# Configurar restricciones
restricciones = {'type': 'eq', 'fun': restriccion}

# Resolver
resultado = minimize(objetivo, [0, 0, 0], constraints=restricciones, method='SLSQP')

# Mostrar resultados
print("Óptimo encontrado:", resultado.fun)
print("Valores óptimos de x, y, z:", resultado.x)

# Graficar la solución en 3D
try:
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Crear una malla para x e y
    x = np.linspace(0, 100, 30)
    y = np.linspace(0, 100, 30)
    X, Y = np.meshgrid(x, y)

    # Resolver para Z usando la restricción
    z_expr = sp.solve(const_expr, sp.Symbol('z'))[0]
    Z = sp.lambdify([sp.Symbol('x'), sp.Symbol('y')], z_expr, 'numpy')(X, Y)

    # Graficar la superficie de restricción
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

    # Graficar el punto óptimo
    ax.scatter(resultado.x[0], resultado.x[1], resultado.x[2], color='red', s=100, label='Punto óptimo')

    # Configurar etiquetas y título
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Superficie de restricción y punto óptimo')

    # Añadir una barra de color
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.legend()
    plt.show()

except Exception as e:
    print(f"Error al generar el gráfico: {str(e)}")

# Validación
print("\nValidación:")
x_opt, y_opt, z_opt = resultado.x
print(f"Valor de la restricción en el óptimo: {const_func(x_opt, y_opt, z_opt)}")
print(f"Valor de la función objetivo en el óptimo: {obj_func(x_opt, y_opt, z_opt)}")