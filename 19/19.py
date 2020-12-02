import sys
import intcode
import numpy as np
import itertools
code = [int(i) for i in sys.stdin.read().split(",")]

def check(i, j): return intcode.intcode(code, [i, j]) == [1]

a = np.zeros((50, 50), "i4")
n = 0
for i, j in np.ndindex(*a.shape):
	a[i, j] = check(i, j)
print(a.sum())

x = 0
for y in itertools.count(100):
	while not check(y, x): x += 1
	if check(y-100, x+100):
		print(x*10000 + y-100)
		break
