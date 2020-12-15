init = tuple(int(x) for x in open("15.in").read().strip().split(","))

# In global scope, this takes 12s
# In function, it takes 8s
# In jit function, it takes 4s
from numba import jit
@jit
def run(init, n):
	last = {}
	for i, a in enumerate(init):
		last[a] = i
	for i in range(i, n-1):
		if i % 1000000 == 0: print("...", i)
		last[a], a = i, i - last.get(a, i)
	return a

# Part 1
print(run(init, 2020))

# Part 2
print(run(init, 30000000))
