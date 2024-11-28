import sympy as sp

# Definir las variables
x, y, λ = sp.symbols('x y λ')  # Variables x, y y el multiplicador de Lagrange

# Definir la función objetivo y la restricción
f = x + y  # Función objetivo
g = x**2 + y**2 - 1  # Restricción: círculo unitario

# Definir la función de Lagrange
L = f + λ * g

# Derivar parcialmente con respecto a x, y y λ
L_x = sp.diff(L, x)  # Derivada respecto a x
L_y = sp.diff(L, y)  # Derivada respecto a y
L_λ = sp.diff(L, λ)  # Derivada respecto a λ

# Resolver el sistema de ecuaciones
soluciones = sp.solve([L_x, L_y, L_λ], [x, y, λ])

# Mostrar las soluciones
for sol in soluciones:
    x_opt, y_opt, λ_opt = sol
    f_opt = f.subs({x: x_opt, y: y_opt})  # Evaluar la función objetivo
    print(f"Solución encontrada: x = {x_opt}, y = {y_opt}, λ = {λ_opt}, f(x, y) = {f_opt}")

import matplotlib.pyplot as plt
import numpy as np

# Graficar la restricción (círculo unitario)
theta = np.linspace(0, 2 * np.pi, 100)
x_circle = np.cos(theta)
y_circle = np.sin(theta)

plt.figure(figsize=(6, 6))
plt.plot(x_circle, y_circle, label="x^2 + y^2 = 1 (restricción)", color="blue")
plt.scatter([sp.N(sol[0]) for sol in soluciones], [sp.N(sol[1]) for sol in soluciones], color="red", label="Soluciones óptimas")
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.axis("equal")
plt.title("Soluciones óptimas y restricción")
plt.show()
