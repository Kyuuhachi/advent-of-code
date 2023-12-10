import numpy as np
input = np.array([list(i) for i in open("10.in").read().splitlines()])
input = np.pad(input, 1, constant_values=".")
[[y], [x]] = np.where(input == "S")
l = np.pad(np.isin(input, list("SJ7-")), ((0, 0), (0, 1)))
r = np.pad(np.isin(input, list("SLF-")), ((0, 0), (1, 0)))
u = np.pad(np.isin(input, list("SJL|")), ((0, 1), (0, 0)))
d = np.pad(np.isin(input, list("S7F|")), ((1, 0), (0, 0)))
h, v = l & r, u & d

vis = np.zeros_like(input, dtype=bool)
n = 0
while True:
	vis[y,x] = True
	if   h[y,x+1] and not vis[y,x+1]: x += 1
	elif h[y,x+0] and not vis[y,x-1]: x -= 1
	elif v[y+1,x] and not vis[y+1,x]: y += 1
	elif v[y+0,x] and not vis[y-1,x]: y -= 1
	else: break
	n += 1
print((n+1)//2)

g = np.zeros((vis.shape[0] * 2+1, vis.shape[1] * 2+1), dtype=bool)
g[1::2,1::2] = vis
g[::2,1::2] = v
g[1::2,::2] = h

q = [(0, 0)]
for y, x in q:
	if g[y, x]: continue
	g[y, x] = True
	q.append((y-1,x))
	q.append((y+1,x))
	q.append((y,x-1))
	q.append((y,x+1))

print((~g[1::2,1::2]).sum())
