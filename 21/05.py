import numpy as np

inp = [
	tuple(
		tuple(map(int, b.split(",")))
		for b in line.split(" -> ")
	) for line in open("05.in")
]

def r(a: int, b: int) -> list[int]:
	if a > b: return list(range(b, a+1))[::-1]
	else:     return list(range(a, b+1))

N = np.max(inp) + 1
a = np.zeros((N, N), "u4")
b = np.zeros((N, N), "u4")
for ((x1,y1),(x2,y2)) in inp:
	if x1 == x2 or y1 == y2:
		a[r(y1,y2), r(x1,x2)] += 1
	b[r(y1,y2), r(x1,x2)] += 1
print((a>1).sum())
print((b>1).sum())
