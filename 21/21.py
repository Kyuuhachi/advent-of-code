import numpy as np
np.set_printoptions(edgeitems=15, linewidth=230)

with open("21.in") as f:
	a = int(f.readline().removeprefix("Player 1 starting position: "))-1
	b = int(f.readline().removeprefix("Player 2 starting position: "))-1

d = 0
(pa, sa, pb, sb) = (a, 0, b, 0)
while True:
	pa += 3*d+6
	d += 3
	sa += 1+pa%10
	if sa >= 1000: break
	(pa, sa, pb, sb) = (pb, sb, pa, sa)
print(sb*d)

g = np.zeros((10, 21, 10, 21), dtype="u8")
g[a, 0, b, 0] = 1
wa, wb = 0, 0
while g.sum():
	g = np.roll(g, 1, 0) + np.roll(g, 2, 0) + np.roll(g, 3, 0)
	g = np.roll(g, 1, 0) + np.roll(g, 2, 0) + np.roll(g, 3, 0)
	g = np.roll(g, 1, 0) + np.roll(g, 2, 0) + np.roll(g, 3, 0)
	for a in range(10):
		x = np.roll(np.pad(g[a], ((0, a+1), (0, 0), (0, 0))), a+1, 0)
		wa += int(x[-a-1:].sum())
		g[a] = x[:-a-1]
	g = np.moveaxis(g, (0,1), (2,3))
	wa, wb = wb, wa
print(max(wa, wb))
