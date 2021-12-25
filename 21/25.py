import numpy as np
g = np.array([[{".": 0, ">": 2, "v": 1}[a] for a in a.strip()] for a in open("25.in")])

i = 0
while True:
	i += 1
	a = (g == 2) & (np.roll(g, -1, 1) == 0)
	g[a], g[np.roll(a, 1, 1)] = 0, 2
	b = (g == 1) & (np.roll(g, -1, 0) == 0)
	g[b], g[np.roll(b, 1, 0)] = 0, 1
	if not (a|b).any():
		break

print(i)
