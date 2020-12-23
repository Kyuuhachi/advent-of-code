inp = [int(a)-1 for a in open("23.in").read().strip()]

import numba
@numba.njit
def run(inp, nmove):
	s = [-1 for _ in inp]
	for a, b in zip(inp, inp[1:]+inp[:1]):
		s[a] = b

	pos = inp[0]
	for _ in range(nmove):
		dest = (pos-1) % len(s)
		if dest == -1: dest += len(s)
		while dest in (s[pos], s[s[pos]], s[s[s[pos]]]):
			dest = (dest-1) % len(s)

		plus3 = s[s[s[pos]]]
		s[plus3], s[dest], s[pos] = s[dest], s[pos], s[plus3]
		pos = s[pos]

	p = s[0]
	while p != 0:
		yield p + 1
		p = s[p]
	
print("".join(map(str, run(inp, 100))))

x = run(inp + list(range(len(inp), 1000000)), 10000000)
print(next(x) * next(x))
