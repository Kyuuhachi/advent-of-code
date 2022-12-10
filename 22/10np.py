import numpy as np
xs = []
x = 1
for word in open("10.in").read().split():
	xs.append(x)
	if word not in ("noop", "addx"):
		x += int(word)
xs = np.array(xs)

i = np.arange(len(xs))
print(np.sum((xs*(i+1))[i%40==19]))
print(np.where(np.isin(xs-i%40, [-1,0,1]), "█", "░").view("U40"))
