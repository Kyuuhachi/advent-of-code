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

print(((v[:-1] & vis).cumsum(axis=1) & ~vis).sum())
