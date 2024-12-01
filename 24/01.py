from collections import Counter
a, b = [], []
for line in open("01.in").read().splitlines():
	v1, v2 = line.split()
	a.append(int(v1))
	b.append(int(v2))

print(sum(abs(v1 - v2) for v1, v2 in zip(sorted(a), sorted(b))))
counts = Counter(b)
print(sum(v1 * counts[v1] for v1 in a))
