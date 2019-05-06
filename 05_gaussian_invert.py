import numpy as np
import copy

def max(arr):
	mxi = 0
	for i in range(1, len(arr)):
		if abs(arr[i]) > abs(arr[mxi]):
			mxi = i
	return mxi, arr[mxi]
		
a = np.array([[0, 1, -1], [-2, 4, -1], [-2, 5, -4]], dtype=np.float32)
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
print('aub :\n', aub)
print('a :\n', a)
print('inv :\n', inv)
print('a x inv :\n', np.dot(a, inv))