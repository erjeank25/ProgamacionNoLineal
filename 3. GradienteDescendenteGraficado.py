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

# Solicitar función objetivo al usuario
while True:
    try:
        obj_str = input("Ingrese la función objetivo (use x, y, z como variables): ")
        obj_expr = parse_expression(obj_str)
        objetivo = create_function(obj_expr)
        break
    except:
        print("Expresión inválida. Por favor, intente de nuevo.")

# Solicitar gradientes al usuario
gradientes = []
for var in ['x', 'y', 'z']:
    while True:
        try:
            grad_str = input(f"Ingrese el gradiente respecto a {var}: ")
            grad_expr = parse_expression(grad_str)
            gradientes.append(create_function(grad_expr))
            break
        except:
            print("Expresión inválida. Por favor, intente de nuevo.")

def gradiente(x, y, z):
    return np.array([g(x, y, z) for g in gradientes])

# Solicitar parámetros al usuario
alpha = float(input("Ingrese el tamaño del paso (alpha): "))
x0 = float(input("Ingrese el valor inicial para x: "))
y0 = float(input("Ingrese el valor inicial para y: "))
z0 = float(input("Ingrese el valor inicial para z: "))
iteraciones = int(input("Ingrese el número de iteraciones: "))

# Listas para almacenar los resultados
puntos = [(x0, y0, z0)]
valores = [objetivo(x0, y0, z0)]

# Gradiente descendente
x, y, z = x0, y0, z0
for i in range(iteraciones):
    grad = gradiente(x, y, z)
    x -= alpha * grad[0]
    y -= alpha * grad[1]
    z -= alpha * grad[2]
    puntos.append((x, y, z))
    valores.append(objetivo(x, y, z))
    if np.linalg.norm(grad) < 1e-6:  # Criterio de parada
        break

# Convertir listas a arrays de NumPy para facilitar la graficación
puntos = np.array(puntos)
valores = np.array(valores)

# Imprimir resultados
print(f"Mínimo encontrado: {valores[-1]}")
print(f"Punto óptimo (x, y, z): {puntos[-1]}")

# Graficar la evolución del valor de la función
plt.figure(figsize=(10, 6))
plt.plot(range(len(valores)), valores, 'b-')
plt.title('Evolución del valor de la función f(x,y,z)')
plt.xlabel('Iteraciones')
plt.ylabel('f(x,y,z)')
plt.grid(True)
plt.show()

# Graficar la trayectoria en 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Crear una malla para la superficie
x = y = np.linspace(min(puntos[:, 0])-1, max(puntos[:, 0])+1, 100)
X, Y = np.meshgrid(x, y)
Z = objetivo(X, Y, puntos[-1, 2])  # Usamos el valor final de z para la visualización

# Graficar la superficie
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

# Graficar la trayectoria de los puntos
ax.plot(puntos[:, 0], puntos[:, 1], puntos[:, 2], 'ro-', label='Trayectoria')
ax.scatter(puntos[0, 0], puntos[0, 1], puntos[0, 2], color='g', s=100, label='Punto inicial')
ax.scatter(puntos[-1, 0], puntos[-1, 1], puntos[-1, 2], color='r', s=100, label='Punto final')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Trayectoria del gradiente descendente')
ax.legend()

plt.colorbar(surf, shrink=0.5, aspect=5)
plt.show()