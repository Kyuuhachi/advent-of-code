import numpy as np
cubes = []
for l in open("22.in"):
	s_, xs__, ys__, zs__ = l.replace(",", " ").split()
	xs_ = [int(a) for a in xs__[2:].split("..")]
	ys_ = [int(a) for a in ys__[2:].split("..")]
	zs_ = [int(a) for a in zs__[2:].split("..")]
	cubes.append((s_ == "on", (xs_[0], xs_[1]+1), (ys_[0], ys_[1]+1), (zs_[0], zs_[1]+1)))

a = np.zeros((101,101,101), dtype="bool")
for s, (x0,x1), (y0,y1), (z0,z1) in cubes:
	if not (-50 <= x0 < x1 <= 51): continue
	a[x0+50:x1+50,y0+50:y1+50,z0+50:z1+50] = s
print(a.sum())

xs = sorted({v2 for _, v, _, _ in cubes for v2 in v})
ys = sorted({v2 for _, _, v, _ in cubes for v2 in v})
zs = sorted({v2 for _, _, _, v in cubes for v2 in v})

a = np.zeros((len(xs)-1, len(ys)-1, len(zs)-1), dtype="bool")
sz \
	= np.diff(np.array(xs, dtype="u8"))[:,None,None] \
	* np.diff(np.array(ys, dtype="u8"))[None,:,None] \
	* np.diff(np.array(zs, dtype="u8"))[None,None,:]
assert a.shape == sz.shape

for s, (x0,x1), (y0,y1), (z0,z1) in cubes:
	a[xs.index(x0):xs.index(x1),ys.index(y0):ys.index(y1),zs.index(z0):zs.index(z1)] = s
print(sz[a].sum())
