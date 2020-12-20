import numpy as np
tiles = {}
for chunk in open("20.in").read().split("\n\n"):
	[fst, *lines] = chunk.splitlines()
	n = int(fst[5:-1])
	assert n != 0
	tiles[n] = np.array([[a == "#" for a in line] for line in lines])

def turn(v):
	return [
		np.rot90(w, n)
		for w in [v, v[::-1]]
		for n in range(4)
	]

from collections import defaultdict
edges = defaultdict(list)
bits = 1<<np.arange(10)
for n, v in tiles.items():
	for w in turn(v):
		edges[w[-1] @ bits].append(n)

# Part 1

from collections import Counter
(a, _), (b, _), (c, _), (d, _) = Counter([
	v[0] for k, v in edges.items() if len(v) == 1
]).most_common(4)
print(a * b * c * d)

# Part 2
corner = tiles[a]
while [len(edges[x[0] @ bits]) for x in turn(corner)[:4]] != [1,2,2,1]:
	corner = np.rot90(corner)

remaining = set(tiles) - {a}
def find(row):
	for x in edges[row @ bits]:
		if x in remaining:
			for v in turn(tiles[x]):
				if (v[0] == row).all():
					remaining.remove(x)
					return v
	raise ValueError(row)

n = int(len(tiles)**(1/2))
assert len(tiles) == n*n
w = np.full((n,n,*corner.shape), 2, "u1")

for y in range(n):
	for x in range(n):
		if   x > 0: w[y,x] = find(w[y,x-1][:,-1]).T
		elif y > 0: w[y,x] = find(w[y-1,x][-1,:])
		else:       w[y,x] = corner
w = w[:,:,1:-1,1:-1].swapaxes(1,2).reshape(n*8,n*8)

monster = """
..................#.
#....##....##....###
.#..#..#..#..#..#...
""".strip()
monster = np.array([[a == "#" for a in line] for line in monster.splitlines()])

mask = np.zeros_like(w)
for m in turn(monster):
	my, mx = np.where(m)
	for y in range(w.shape[0]-m.shape[0]):
		for x in range(w.shape[1]-m.shape[1]):
			if w[my+y,mx+x].all():
				mask[my+y,mx+x] = True

print((w & ~mask).sum())
