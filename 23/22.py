import numpy as np
from numpy import ma
bricks = []
for i, line in enumerate(open("22.in").read().splitlines()):
	p1,p2 = line.split("~")
	x1,z1,y1 = map(int, p1.split(","))
	x2,z2,y2 = map(int, p2.split(","))
	bricks.append(((x1,x2),(z1,z2),(y1,y2), i))
bricks.sort(key=lambda a: a[2])

height = np.zeros((10, 10), dtype="u4")
top = np.full((10, 10), -1, dtype="i4")
can = np.ones(len(bricks), dtype=bool)
supported_by = {}
for x,z,y,i in bricks:
	s = np.s_[x[0]:x[1]+1,z[0]:z[1]+1]
	h = height[s].max()
	sup = np.unique(top[s][(height[s] == h)])
	supported_by[i] = set(sup)
	if len(sup) == 1 and sup[0] != -1:
		can[sup] = False
	assert h <= y[0], (h, (x,z,y,i))
	height[s] = h + y[1] + 1 - y[0]
	top[s] = i
print(can.sum())

n = 0
for i in range(len(bricks)):
	broken = {i}
	p = 0
	while len(broken) != p:
		p = len(broken)
		for j in range(len(bricks)):
			if not (supported_by[j] - broken):
				broken.add(j)
	n += len(broken) - 1
print(n)
