import numpy as np
import copy

def max(arr):
	mxi = 0
	for i in range(1, len(arr)):
		if abs(arr[i]) > abs(arr[mxi]):
			mxi = i
	return mxi, arr[mxi]

def invert(arr):
	a = copy.deepcopy(arr)
	(r, c) = a.shape
	b = np.eye(c, dtype=np.float32)
	aub = np.hstack([a, b])
	for i in range(c-1):
		col = aub[i:c, i]
		p, v = max(col.tolist())
		tmp = copy.deepcopy(aub[i, :])
		aub[i, :] = copy.deepcopy(aub[p+i, :])
		aub[p+i, :] = copy.deepcopy(tmp)
	for i in range(c):
		aub[i, :] = aub[i, :] / aub[i, i]
		for j in range(i+1, c):
			aub[j, :] = aub[j, :] - aub[j, i] * aub[i, :]
	for i in range(1, c):
		for j in range(i):
			aub[j, :] = aub[j, :] - aub[j, i] * aub[i, :]
	inv = copy.deepcopy(aub[:, c:])
	return inv

x = [1, 2, 3, 4, 5]
y = [2, 5, 3, 8, 7]
n = len(y)
ml = np.zeros((n, n), dtype=np.float32)
mr = np.zeros((n, 1), dtype=np.float32)
for r in range(n):
	for c in range(n):
		ml[r, c] = sum(map(lambda a: a**(r + c), x))
	mr[r] = sum(map(lambda a, b: a * b**r, y, x))
a = np.dot(invert(ml), mr)
print(a)