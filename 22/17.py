import numpy as np
wind = [{"<": -1, ">": 1}[c] for c in open("17.in").read().strip()]

shapes = [
	np.array([[0,0,0,1,1,1,1,0,0]], dtype=bool),
	np.array([[0,0,0,0,1,0,0,0,0],
	          [0,0,0,1,1,1,0,0,0],
	          [0,0,0,0,1,0,0,0,0]], dtype=bool),
	np.array([[0,0,0,0,0,1,0,0,0],
	          [0,0,0,0,0,1,0,0,0],
	          [0,0,0,1,1,1,0,0,0]], dtype=bool),
	np.array([[0,0,0,1,0,0,0,0,0],
	          [0,0,0,1,0,0,0,0,0],
	          [0,0,0,1,0,0,0,0,0],
	          [0,0,0,1,0,0,0,0,0]], dtype=bool),
	np.array([[0,0,0,1,1,0,0,0,0],
	          [0,0,0,1,1,0,0,0,0]], dtype=bool),
]

def run(n):
	well = np.zeros((16, 9), dtype=bool)
	well[0] = True
	well[:,0] = True
	well[:,-1] = True
	h = 1
	t = 0
	xs = []
	for s in range(n):
		piece = shapes[s % 5][::-1]
		y = h + 3
		while len(well) < y + len(piece):
			well = np.concatenate([well, np.zeros_like(well)])
			well[:,0] = True
			well[:,-1] = True

		h0 = h
		while True:
			drift = wind[t%len(wind)]
			t += 1
			piece2 = np.roll(piece, drift, axis=1)
			if not (well[y:y+len(piece)] & piece2).any():
				piece = piece2

			y -= 1

			if (well[y:y+len(piece)] & piece).any():
				y += 1
				well[y:y+len(piece)] |= piece
				h = max(h, y+len(piece))
				break
		xs.append(h-h0)
	return xs
print(sum(run(2022)))

xs = run(10000)
for i in range(10, len(xs)):
	if xs[-i:] == xs[-i*2:-i]:
		break

rep = xs[-i:]
n = 1000_000_000_000
a, b = divmod(n - len(xs), len(rep))
print(sum(xs) + sum(rep) * a + sum(rep[:b]))
