import numpy as np
from collections import Counter
inp = {
	(y, x)
	for y, l in enumerate(open("23.in").read().splitlines())
	for x, c in enumerate(l)
	if c == '#'
}

r = [
	[[-1,0],[-1,-1],[-1,+1]],
	[[+1,0],[+1,-1],[+1,+1]],
	[[0,-1],[-1,-1],[+1,-1]],
	[[0,+1],[-1,+1],[+1,+1]],
]

pos = inp
t = 0
while True:
	prop = {p: p for p in pos}
	for (y,x) in pos:
		if any((y+dy,x+dx) in pos for dy in (-1,0,1) for dx in (-1,0,1) if dx or dy):
			for w in r:
				if not any((y+dy,x+dx) in pos for dy, dx in w):
					prop[(y,x)] = (y+w[0][0],x+w[0][1])
					break

	r.append(r.pop(0))
	t += 1

	count = Counter(prop.values())
	pos2 = {prop[p] if count[prop[p]] == 1 else p for p in pos}
	if pos2 == pos:
		print(t)
		break
	pos = pos2

	if t == 10:
		mny = min(p[0] for p in pos)
		mxy = max(p[0] for p in pos)
		mnx = min(p[1] for p in pos)
		mxx = max(p[1] for p in pos)

		g = np.zeros((mxy-mny+1, mxx-mnx+1), dtype=bool)
		for y,x in pos:
			g[y-mny,x-mnx] = True
		# print(np.where(g, '█', '░').view(f"U{g.shape[-1]}"))
		print((~g).sum())

	if t % 10 == 0:
		print(f"({t})")
