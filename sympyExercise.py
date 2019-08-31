import sympy

# Sympy

# differential(微分) ####################################
x = sympy.Symbol('x')
y = sympy.Symbol('y')
print(type(x))

expr = x ** 2 + y + 1
print(expr)

print(sympy.diff(expr, x))
print(sympy.diff(expr, y))

print(sympy.factor(x ** 3 - x ** 2 - 3 * x + 3))


# integrate(積分) ####################################
print(sympy.integrate(3 * x**2 + 4 * x + 1))
