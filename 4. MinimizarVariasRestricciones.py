import cvxpy as cp
import sympy as sp

def parse_expression(expr_str):
    x = sp.Symbol('x')
    return sp.sympify(expr_str)

def create_cvxpy_expression(expr, x):
    return eval(str(expr), {'x': x, 'cp': cp})

# Solicitar función objetivo
obj_str = input("Ingrese la función objetivo (use 'x' como variable): ")
obj_expr = parse_expression(obj_str)

# Determinar si es un problema de maximización o minimización
problem_type = input("¿Desea maximizar o minimizar? (max/min): ").lower()
while problem_type not in ['max', 'min']:
    problem_type = input("Por favor, ingrese 'max' o 'min': ").lower()

# Solicitar restricciones
restricciones = []
while True:
    const_str = input("Ingrese una restricción (o 'fin' para terminar): ")
    if const_str.lower() == 'fin':
        break
    const_expr = parse_expression(const_str)
    restricciones.append(const_expr)

# Crear variable CVXPY
x = cp.Variable()

# Crear función objetivo CVXPY
obj_cvxpy = create_cvxpy_expression(obj_expr, x)

# Crear restricciones CVXPY
const_cvxpy = [create_cvxpy_expression(const, x) >= 0 for const in restricciones]

# Crear el problema
if problem_type == 'max':
    objetivo = cp.Maximize(obj_cvxpy)
else:
    objetivo = cp.Minimize(obj_cvxpy)

problema = cp.Problem(objetivo, const_cvxpy)

# Resolver el problema
problema.solve()

# Mostrar resultados
print(f"Estado: {problema.status}")
if problem_type == 'max':
    print(f"Máximo: {problema.value}")
else:
    print(f"Mínimo: {problema.value}")
print(f"Valor óptimo de x: {x.value}")

# Verificar las restricciones
print("\nVerificación de restricciones:")
for i, const in enumerate(restricciones):
    valor = const.subs('x', x.value)
    print(f"g{i+1}(x) = {const} = {valor}")