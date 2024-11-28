import sympy as sp
import cvxpy as cp
import numpy as np

def obtener_funcion_usuario(prompt):
    while True:
        try:
            expr_str = input(prompt)
            x, y = sp.symbols('x y')
            expr = sp.sympify(expr_str)
            return expr, expr_str
        except sp.SympifyError:
            print("Expresión inválida. Por favor, intente de nuevo.")

def obtener_restricciones():
    restricciones = []
    restricciones_str = []
    while True:
        tipo = input("Ingrese el tipo de restricción (igualdad/desigualdad) o 'fin' para terminar: ").lower()
        if tipo == 'fin':
            break
        elif tipo in ['igualdad', 'desigualdad']:
            expr, expr_str = obtener_funcion_usuario(f"Ingrese la restricción de {tipo} (use x e y): ")
            restricciones.append((expr, tipo))
            restricciones_str.append(expr_str)
        else:
            print("Tipo de restricción no válido. Use 'igualdad' o 'desigualdad'.")
    return restricciones, restricciones_str

def formular_lagrange(objetivo, restricciones):
    x, y = sp.symbols('x y')
    lambdas = sp.symbols(' '.join([f'λ{i+1}' for i in range(len(restricciones))]))
    
    L = objetivo
    for i, (r, tipo) in enumerate(restricciones):
        L += lambdas[i] * r

    derivadas = [sp.diff(L, var) for var in [x, y] + list(lambdas)]
    
    print("\na. Formulación como un problema de Lagrange con múltiples restricciones:")
    print("Función de Lagrange:")
    print(f"L = {L}")
    print("\nEcuaciones de Lagrange:")
    for i, d in enumerate(derivadas):
        print(f"∂L/∂{[x, y] + list(lambdas)}[{i}] = {d} = 0")

def resolver_cvxpy(objetivo_str, restricciones_str):
    x = cp.Variable()
    y = cp.Variable()

    # Convertir la función objetivo a una expresión CVXPY
    objetivo_cvxpy = eval(objetivo_str, {'x': x, 'y': y, 'cp': cp})
    
    # Convertir las restricciones a expresiones CVXPY
    restricciones_cvxpy = []
    for r_str in restricciones_str:
        if '<=' in r_str:
            lhs, rhs = r_str.split('<=')
            restricciones_cvxpy.append(eval(lhs, {'x': x, 'y': y, 'cp': cp}) <= eval(rhs, {'x': x, 'y': y, 'cp': cp}))
        elif '>=' in r_str:
            lhs, rhs = r_str.split('>=')
            restricciones_cvxpy.append(eval(lhs, {'x': x, 'y': y, 'cp': cp}) >= eval(rhs, {'x': x, 'y': y, 'cp': cp}))
        elif '==' in r_str:
            lhs, rhs = r_str.split('==')
            restricciones_cvxpy.append(eval(lhs, {'x': x, 'y': y, 'cp': cp}) == eval(rhs, {'x': x, 'y': y, 'cp': cp}))
        else:
            # Si no hay operador de comparación, asumimos que es una desigualdad <= 0
            restricciones_cvxpy.append(eval(r_str, {'x': x, 'y': y, 'cp': cp}) <= 0)

    problema = cp.Problem(cp.Maximize(objetivo_cvxpy), restricciones_cvxpy)
    
    try:
        resultado = problema.solve()
        print("\nb. Resolución utilizando CVXPY:")
        print("Estado:", problema.status)
        print("Valor óptimo:", problema.value)
        print("Solución óptima:")
        print(f"x = {x.value}")
        print(f"y = {y.value}")

    except cp.error.SolverError:
        print("\nError: No se pudo resolver el problema.")
        print("Esto puede deberse a restricciones incompatibles o a un problema mal formulado.")
        print("Por favor, revise sus restricciones y asegúrese de que el problema tenga una solución factible.")

if __name__ == "__main__":
    print("Bienvenido al optimizador de inversiones flexible.")
    objetivo, objetivo_str = obtener_funcion_usuario("Ingrese la función objetivo a maximizar (use x e y): ")
    restricciones, restricciones_str = obtener_restricciones()

    formular_lagrange(objetivo, restricciones)
    resolver_cvxpy(objetivo_str, restricciones_str)