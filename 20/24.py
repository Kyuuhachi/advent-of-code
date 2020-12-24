import numpy as np
dirs = {
	"nw": ( 0,-1),
	"w":  (-1, 0),
	"sw": (-1,+1),
	"se": ( 0,+1),
	"e":  (+1, 0),
	"ne": (+1,-1),
}
pos = []
for line in open("24.in").read().splitlines():
	n = np.array((0,0))
	for ch in (it := iter(line)):
		if ch in "ns": ch += next(it)
		n += dirs[ch]
	pos.append(n)
pos = np.array(pos)
pos -= np.min(pos, axis=0)

# Part 1
g = np.zeros(np.max(pos, axis=0)+1, bool)
for a, b in pos:
	g[a, b] ^= True
print(g.sum())

# Part 2
slices = [slice(2,None), slice(1,-1), slice(0,-2)]
shifts = [(slices[a+1], slices[b+1]) for a, b in dirs.values()]
for _ in range(100):
	g = np.pad(g, 1)
	q = np.pad(g, 1)
	y = np.array([q[a] for a in shifts]).sum(axis=0)
	g = (y == 2) | g & (y == 1)
print(g.sum())
