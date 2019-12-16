import numpy as np
inp = input()
off = int(inp[:7])
a = np.array([int(x) for x in inp])

b = np.zeros((a.size, a.size), "int")
for i in range(a.size):
	b[i] = np.tile(np.repeat([0,1,0,-1], i+1), a.size)[1:a.size+1]

a1 = a
for _ in range(100):
	a1 = np.abs(b@a1)%10
print(a1[:8])

assert off > len(a)*30000//4
a1 = np.tile(a, 10000)[off:]
for a in range(100):
	a1 = np.cumsum(a1[::-1])[::-1]%10
print(a1[:8])
