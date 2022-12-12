import numpy as np
inp = np.array([[0 if c == 'S' else 27 if c == 'E' else ord(c)-ord('a')+1 for c in line] for line in open("12.in").read().splitlines()], dtype="u8")
inp = np.pad(inp, 1, constant_values=99)

s = inp == 0
e = inp == 27
inp[s] = 1
inp[e] = 26
inp -= 1

m = np.full_like(inp, -1, dtype="i4")
m[[0,-1],:] = -2
m[:,[0,-1]] = -2

[(y,x)] = np.argwhere(e)
m[y,x] = 0
queue = [(y,x)]
for (y, x) in queue:
	for y2, x2 in (y-1,x),(y,x-1),(y+1,x),(y,x+1):
		if m[y2, x2] == -1 and inp[y2,x2] >= inp[y,x]-1:
			m[y2, x2] = m[y, x]+1
			queue.append((y2, x2))

print(m[s][0])
print(m[(inp==0) & (m != -1)].min())
