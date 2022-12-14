import numpy as np
inp = []
for line in open("14.in"):
	inp.append([eval(f"({a})")[::-1] for a in line.split()[::2]])

y0 = min([0] + [a[0] for a in inp for a in a])
y1 = max([0] + [a[0] for a in inp for a in a])+1
x0 = min([500] + [a[1] for a in inp for a in a])-1
x1 = max([500] + [a[1] for a in inp for a in a])+2

g = np.zeros((y1-y0, x1-x0), bool)
for l in inp:
	for (a,b),(c,d) in zip(l, l[1:]):
		g[min(a,c)-y0:max(a,c)-y0+1, min(b,d)-x0:max(b,d)-x0+1] = True

def sand(g, y0, x0):
	h = np.array(g)
	n = 0
	while True:
		found = False
		y, x = y0, x0
		while True:
			w = np.where(h[y:, x])[0]
			if not len(w): break
			if w[0] == 0: break
			y += w[0]
			if not h[y, x-1]:
				x -= 1
			elif not h[y, x+1]:
				x += 1
			else:
				h[y-1, x] = True
				found = True
				break
		if not found:
			break
		n += 1
	print(np.array(["░", "▒", "█"])[h.view("u1") + g.view("u1")].view(f"U{g.shape[1]}"))
	print(n)
sand(g, 0-y0, 500-x0)

def sand2(g, y0, x0):
	access = np.zeros_like(g[0])
	access[x0] = True
	l, r = 0, 0
	n = 0
	for row in g:
		access &= ~row
		n += access.sum() + l + r
		print(np.array(["░", "▒", "█"])[(access).view("u1") + 2*row.view("u1")].view(f"U{row.shape[0]}"), n)
		if access[0]: l += 1
		if access[-1]: r += 1
		access[1:] |= access[:-1]
		access[:-1] |= access[1:]
	print(n)
sand2(np.pad(g, ((0, 1), (0, 0))), 0-y0, 500-x0)
