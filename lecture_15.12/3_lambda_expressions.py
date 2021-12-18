x = 2
y = 3
z = 4
exponentiation_without_any_lambdas = (x ** y) ** z
print(exponentiation_without_any_lambdas)

exponentiation_with_1_lambda = lambda x, y, z: (x ** y) ** z
print(exponentiation_with_1_lambda(2, 3, 4))

exponentiation_with_2_lambdas = lambda x, y: (lambda z: (x ** y) ** z)
print(exponentiation_with_2_lambdas(2, 3).__call__(4))