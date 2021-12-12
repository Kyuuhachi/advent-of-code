import typing as T
from collections import defaultdict
inp = [tuple(a.strip().split("-")) for a in open("12.in")]

nxt = defaultdict(list)
for a, b in inp:
	nxt[a].append(b)
	nxt[b].append(a)

# For these short paths tuple is faster than set, and also maintains order which
# is nice even though it's not useful here.
def run(pos: str, /, n: int, path: tuple[str, ...] = ()) -> T.Iterator[tuple[str, ...]]:
	path = path + (pos,)
	if pos == "end":
		yield path
		return

	for pos in nxt[pos]:
		if pos == "start":
			pass
		elif pos.isupper() or pos not in path:
			yield from run(pos, n=n, path=path)
		elif n > 0:
			yield from run(pos, n=n-1, path=path)

print(len(list(run("start", n=0))))
print(len(list(run("start", n=1))))
