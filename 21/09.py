import numpy as np
a = np.array([[int(a) for a in line.strip()] for line in open("09.in")])

b = np.pad(a, 1, constant_values=9)
m = np.all([
	a < b[2:,1:-1:],
	a < b[:-2,1:-1:],
	a < b[1:-1:,2:],
	a < b[1:-1:,:-2],
], axis=0)
print((a[m]+1).sum())

s = []
for y, x in np.argwhere(m):
	q = [(y+1, x+1)]
	for (y, x) in q:
		for p2 in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
			if b[p2] != 9 and b[p2] > b[y, x]:
				q.append(p2)
	s.append(len(set(q)))
print(np.product(sorted(s)[-3:]))
