import numpy as np

bricks = []
for line in open("22.in").read().splitlines():
	p1,p2 = line.split("~")
	x1,z1,y1 = map(int, p1.split(","))
	x2,z2,y2 = map(int, p2.split(","))
	bricks.append(((x1,x2),(z1,z2),(y1,y2)))
bricks.sort(key=lambda a: a[2])

height = np.zeros((10, 10), dtype="u4")
top = np.full((10, 10), -1, dtype="i4")
supported_by = []
for i,(x,z,y) in enumerate(bricks):
	s = np.s_[x[0]:x[1]+1,z[0]:z[1]+1]
	h = height[s].max()
	supported_by.append(set(np.unique(top[s][(height[s] == h)])))
	assert h <= y[0]
	height[s] = h + y[1] + 1 - y[0]
	top[s] = i

can = set(range(len(bricks)))
for sup in supported_by:
	if len(sup) == 1:
		can -= sup
print(len(can))

n = 0
for i in range(len(bricks)):
	broken = {i}
	for j in range(i, len(bricks)):
		if supported_by[j] <= broken:
			broken.add(j)
	n += len(broken) - 1
print(n)
