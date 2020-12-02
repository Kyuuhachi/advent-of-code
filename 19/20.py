from collections import defaultdict
import sys
# inp = sys.stdin.read().splitlines()
inp ="""
             Z L X W       C                 
             Z P Q B       K                 
  ###########.#.#.#.#######.###############  
  #...#.......#.#.......#.#.......#.#.#...#  
  ###.#.#.#.#.#.#.#.###.#.#.#######.#.#.###  
  #.#...#.#.#...#.#.#...#...#...#.#.......#  
  #.###.#######.###.###.#.###.###.#.#######  
  #...#.......#.#...#...#.............#...#  
  #.#########.#######.#.#######.#######.###  
  #...#.#    F       R I       Z    #.#.#.#  
  #.###.#    D       E C       H    #.#.#.#  
  #.#...#                           #...#.#  
  #.###.#                           #.###.#  
  #.#....OA                       WB..#.#..ZH
  #.###.#                           #.#.#.#  
CJ......#                           #.....#  
  #######                           #######  
  #.#....CK                         #......IC
  #.###.#                           #.###.#  
  #.....#                           #...#.#  
  ###.###                           #.#.#.#  
XF....#.#                         RF..#.#.#  
  #####.#                           #######  
  #......CJ                       NM..#...#  
  ###.#.#                           #.###.#  
RE....#.#                           #......RF
  ###.###        X   X       L      #.#.#.#  
  #.....#        F   Q       P      #.#.#.#  
  ###.###########.###.#######.#########.###  
  #.....#...#.....#.......#...#.....#.#...#  
  #####.#.###.#######.#######.###.###.#.#.#  
  #.......#.......#.#.#.#.#...#...#...#.#.#  
  #####.###.#####.#.#.#.#.###.###.#.###.###  
  #.......#.....#.#...#...............#...#  
  #############.#.#.###.###################  
               A O F   N                     
               A A D   M                     
""".strip("\n").splitlines()

inp = ["@%s " % l for l in inp]
inp = ["@"*len(inp[0]), *inp, "@"*len(inp[0])]

def find_portals():
	for r in range(len(inp)):
		for c in range(len(inp[r])):
			if 'A' <= inp[r][c] <= 'Z':
				for r2, c2 in [(-1,0), (+1,0), (0,-1), (0,+1)]:
					if 'A' <= inp[r+r2][c+c2] <= 'Z' and inp[r-r2][c-c2] == ".":
						yield r-r2, c-c2, "".join(sorted(inp[r][c]+inp[r+r2][c+c2])), inp[r+r2*2][c+c2*2] == "@"

all_portals = defaultdict(list)
for r, c, name, outer in find_portals():
	all_portals[name].append(((r, c), outer))

[(start, _)] = all_portals.pop("AA")
[(end, _)] = all_portals.pop("ZZ")

names = {}
for k, v in all_portals.items():
	for v, _ in v: names[v] = k

portals = {}
for [(p0, o0), (p1, o1)] in all_portals.values():
	portals[p0] = p1, -1 if o0 else 1
	portals[p1] = p0, -1 if o1 else 1
print(portals)

pos = [(0, start, 0)]
seen = set()
trace = defaultdict(set)
for n, p, l in pos:
	# l = 0 # For part 1
	if (p, l) in seen: continue
	seen.add((p, l))
	trace[n].add((p, l))
	if l < 0: continue
	if (p, l) == (end, 0): break
	r, c = p
	for r2, c2 in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
		if inp[r2][c2] == '.':
			pos.append((n+1, (r2, c2), l))
	if p in portals:
		p2, dl = portals[p]
		pos.append((n+1, p2, l+dl))

print(n)
for n2 in reversed(range(n)):
	r, c = p
	for r2, c2 in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
		if ((r2, c2), l) in trace[n2]:
			p = (r2, c2)
			break
	else:
		p2, dl = portals[p]
		print(f"{names[p]} {dl} {l}")
		print((names[p], l), (names[p2], l-dl), sorted([(names.get(p, p), l) for p, l in trace[n2] if p in names], key=lambda a:a[1]))
		assert (p2, l-dl) in trace[n2]
		p = p2
		l = l-dl
