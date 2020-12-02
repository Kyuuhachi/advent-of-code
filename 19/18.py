import sys
maze = sys.stdin.read().splitlines()

pos = None
allkeys = set()
for r, R in enumerate(maze):
	for c, C in enumerate(R):
		if C == "@": pos = (r, c)
		if 'a' <= C <= 'z': allkeys.add(C)

# states = [(0, pos, frozenset())]
# seen = set()
# for (n, p, k) in states:
# 	if (p, k) in seen: continue
# 	seen.add((p, k))
# 	if k == allkeys: break

# 	r, c = p
# 	for (r, c, k) in [(r+1,c,k), (r-1,c,k), (r,c+1,k), (r,c-1,k)]:
# 		if maze[r][c] == "#": continue
# 		if 'A' <= maze[r][c] <= 'Z' and maze[r][c].lower() not in k: continue
# 		if 'a' <= maze[r][c] <= 'z': k |= {maze[r][c]}
# 		states.append((n+1, (r, c), k))
# print(n)

r,c=pos
extra={(r-1,c),(r+1,c),(r,c+1),(r,c-1)}
for x in [ (r-1, c-1), (r-1, c+1), (r+1, c+1), (r+1, c-1) ]:
	k = set()
	states = [x]
	seen = set()
	for p in states:
		if p in seen: continue
		seen.add(p)

		r, c = p
		for (r, c) in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
			if (r,c) in extra: continue
			if maze[r][c] == "#": continue
			if 'a' <= maze[r][c] <= 'z': k |= {maze[r][c]}
			states.append((r, c))

	states = [(0, x, frozenset(allkeys-k))]
	seen = set()
	for (n, p, k) in states:
		if (p, k) in seen: continue
		seen.add((p, k))
		if k == allkeys: break

		r, c = p
		for (r, c, k) in [(r+1,c,k), (r-1,c,k), (r,c+1,k), (r,c-1,k)]:
			if (r,c) in extra: continue
			if maze[r][c] == "#": continue
			if 'A' <= maze[r][c] <= 'Z' and maze[r][c].lower() not in k: continue
			if 'a' <= maze[r][c] <= 'z': k |= {maze[r][c]}
			states.append((n+1, (r, c), k))
	print(n)
