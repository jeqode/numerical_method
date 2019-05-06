from math import pi, factorial

def f(x):
	return (3*x + 1) ** pi

def P(n, x):
	zigma = 0
	for i in range(n+1):
		prod = 1
		for j in range(1, i+1):
			prod = prod * (3 * (pi - j + 1))
		zigma += prod * (x ** i) / factorial(i)
	return zigma

print('%.10f, %.10f' % (f(2), P(10, 2)))