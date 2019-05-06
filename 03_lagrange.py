x = [2, 2.5, 4]
f = [.5, .4, .25]
xn = 3
n = len(x)

def L(x, xi, t):
	m = 1.
	for i in range(n):
		if (i != xi):
			q = (t - x[i]) / (x[xi] - x[i])
			m = m * q
	return m

def lagrange(x, f, t):
	fn = 0
	for i in range(n):
		fn += f[i] * L(x, i, t)
	return fn

print(lagrange(x, f, xn))