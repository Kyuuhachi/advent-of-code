input = []
for i in open("12.in"):
	a, b = i.split()
	input.append((a, [int(b) for b in b.split(",")]))

def count(a: str, b: list[int]):
	a += '.'
	import functools
	@functools.lru_cache(None)
	def rec(i: int, j: int):
		if i == len(a): return j == len(b)
		if j == len(b): return '#' not in a[i:]
		n = 0
		if a[i] != '.':
			k = i+b[j]
			if len(a) >= k \
					and '.' not in a[i:k] \
					and a[k] != '#':
				n += rec(k+1, j+1)
		if a[i] != '#':
			n += rec(i+1, j)
		return n
	return rec(0, 0)

print(sum(count(a, b) for a, b in input))
print(sum(count(f"{a}?{a}?{a}?{a}?{a}", b * 5) for a, b in input))
