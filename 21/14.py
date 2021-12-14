from collections import Counter
with open("14.in") as f:
	start = next(f).strip()
	next(f)
	lines = [tuple(a.strip().split(" -> ")) for a in f]

between = { tuple(k): v for k, v in sorted(lines) }

def run(niter: int) -> Counter[str]:
	s = Counter(zip(start, start[1:]))
	for _ in range(niter):
		n = Counter()
		for (a, c), v in s.items():
			b = between[a, c]
			n[a, b] += v
			n[b, c] += v
		s = n

	ng = Counter()
	ng[start[-1]] += 1
	for (a, c), v in s.items():
		ng[a] += v
	return ng

a, b = run(10).most_common(), run(40).most_common()
print(a[0][1] - a[-1][1])
print(b[0][1] - b[-1][1])
