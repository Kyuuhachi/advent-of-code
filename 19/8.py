import numpy as np
layers = np.array([int(a) for a in input()]).reshape(-1, 6, 25)

l = layers[(layers==0).sum(axis=(1,2)).argmin()]
print((l==1).sum() * (l==2).sum())

m = np.full_like(layers[0], 2)
for l in layers:
	m[m==2] = l[m==2]
print(str(m).replace("0", "."))
