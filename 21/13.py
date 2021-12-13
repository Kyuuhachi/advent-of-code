import numpy as np
np.set_printoptions(linewidth=123456)
pts = []
fold = []
with open("13.in") as f:
	while l := f.readline().strip():
		pts.append(tuple(int(b) for b in l.split(","))[::-1])
	while l := f.readline():
		w, x = l.removeprefix("fold along ").split("=")
		fold.append((w, int(x)))

size = (np.max(pts, axis=0)+1)|1 # Not sure if this is universal
a = np.zeros(size, dtype=bool)
a[tuple(np.transpose(pts))] = True
for i, (w, x) in enumerate(fold):
	if w == "y": a = a[:x,:] | a[x+1:,:][::-1,:]
	if w == "x": a = a[:,:x] | a[:,x+1:][:,::-1]
	if i == 0: print(a.sum())
print(a.astype(int).__str__().replace("0", "."))
