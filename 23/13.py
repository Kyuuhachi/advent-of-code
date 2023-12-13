import numpy as np
input = [
	np.array([list(i) for i in i.splitlines()]) == '#'
	for i in open("13.in").read().split("\n\n")
]

def refl(p, n):
	for i in range(1, len(p)):
		a, b = p[:i][::-1], p[i:]
		l = min(len(a), len(b))
		if np.count_nonzero(a[:l] != b[:l]) == n:
			return i
	return 0

print(sum(refl(i, 0) * 100 + refl(i.T, 0) for i in input))
print(sum(refl(i, 1) * 100 + refl(i.T, 1) for i in input))
