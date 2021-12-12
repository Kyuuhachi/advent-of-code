from collections import defaultdict
inp = [tuple(a.strip().split("-")) for a in open("12.in")]

nxt = defaultdict(list)
for a, b in inp:
	nxt[a].append(b)
	nxt[b].append(a)

def run(n: int) -> list[list[str]]:
	states = [("start", ["start"], n)]
	while True:
		states2 = []
		for (pos, path, n) in states:
			if pos == "end":
				states2.append((pos, path, n))
			else:
				for b in nxt[pos]:
					m = n
					if not b.isupper() and b in path:
						m -= 1
					if m > 0 and b != "start":
						states2.append((b, path + [b], m))
		if states2 == states:
			break
		states = states2
	return [path for _, path, _ in states]

print(len(run(1)))
print(len(run(2)))
