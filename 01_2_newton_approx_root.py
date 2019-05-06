EPSILON = 0.00000000001

def f(x):
	return 3 * x**4 + 5 * x**3 - 2 * x**2 + 8 * x - 2

def findRoot(mode="abs"):
	def byAbs(m):
		return abs(f(m))
	def byBa(a, b, n):
		return abs( (b - a) / 2**n )
		
	a, b = -1, 2
	found = False
	n =0
	while not found:
		n += 1
		m = (a + b) / 2.0
		ex = byBa(a, b, n) if mode == "ba" else byAbs(m)
		if ex < EPSILON:
			found = True
			return n, m
		if f(a) * f(m) > 0:
			a = m
		else:
			b = m

(absN, absRoot) = findRoot("abs")
(baN, baRoot) = findRoot("ba")
print('abs(f(m)) : #%i f(%.10f) = %.10f' % (absN, absRoot, f(absRoot)))
print('b-a/2**n  : #%i f(%.10f) = %.10f' % (baN, baRoot, f(baRoot)))