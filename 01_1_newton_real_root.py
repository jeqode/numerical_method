def f(x):
	return 3 * x**4 + 5 * x**3 - 2 * x**2 + 8 * x - 2

a, b = -1, 2
left = []
right = []
found = False
while not found:
	m = (a + b) / 2.0
	if f(m) == 0:
		found = True
		break
	if f(a) * f(m) > 0:
		a = m
	else:
		b = m
	if f(m) < 0:
		left.append(m)
	else:
		right.append(m)
print('root is at f(%.20f) = %.20f' % (m, f(m)))
print('Left:')
for i in left[-1:-4:-1]:
	print(' f(%.20f) = %.20f' % (i, f(i)))
print('Right:')
for i in right[-1:-4:-1]:
	print(' f(%.20f) = %.20f' % (i, f(i)))