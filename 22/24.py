import numpy as np
g = np.array([
	list(l[1:-1])
	for l in open("24.in").read().splitlines()[1:-1]
])

lf = g == '<'
rg = g == '>'
up = g == '^'
dn = g == 'v'

bliz = np.array([
	np.roll(lf, -i, 1)
	| np.roll(rg, i, 1)
	| np.roll(up, -i, 0)
	| np.roll(dn, i, 0)
	for i in range(np.lcm(*g.shape))
])
bliz = np.pad(bliz, ((0,0),(1,1),(1,1)), "constant", constant_values=True)
bliz[:,0,1] = False
bliz[:,-1,-2] = False

d = np.zeros((3, *bliz.shape), dtype="u2")
d[:, bliz] = -1

d[0,0,0,1] = 1
q = [(0,0,0,1)]
for k,t,y,x in q:
	w = [(y,x)]
	if y == 0:
		w.append((y+1,x))
		if k == 1:
			d[2,t,y,x] = d[1,t,y,x]
			k = 2
	elif y == bliz.shape[-2]-1:
		w.append((y-1,x))
		if k == 0:
			d[1,t,y,x] = d[0,t,y,x]
			k = 1
	else:
		w.append((y-1,x))
		w.append((y+1,x))
		w.append((y,x-1))
		w.append((y,x+1))

	T = (t + 1) % len(bliz)
	for y0,x0 in w:
		if not d[k,T,y0,x0]:
			d[k,T,y0,x0] = d[k,t,y,x]+1
			q.append((k,T,y0,x0))

e = d[0,:,-1,-2]
print((e-1).min())
e = d[2,:,-1,-2]
print((e-1).min())
