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

for i in range(c-1):
	col = a[i:c, i]
	p, v = max(col.tolist())
	tmp = copy.deepcopy(a[i, :])
	a[i, :] = copy.deepcopy(a[p+i, :])
	a[p+i, :] = copy.deepcopy(tmp)

for i in range(c-1):
	for j in range(i+1, c):
		m = a[j, i] / a[i, i]
		a[j, :] = a[j, :] - m * a[i, :]

det = 1
for i in range(c):
	det = det * a[i, i]

print(a)
print(det)