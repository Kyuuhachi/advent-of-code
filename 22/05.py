import copy
inp_crates, inp_moves = open("05.in").read().split("\n\n")
inp_crates = inp_crates.splitlines()[::-1]

crates = [[] for _ in range(len(inp_crates[0][1::4]))]
for line in inp_crates[1:]:
	for i, x in enumerate(line[1::4]):
		if x != ' ':
			crates[i].append(x)

crates2 = copy.deepcopy(crates)
for line in inp_moves.splitlines():
	a, b, c = map(int, line.split()[1::2])
	for _ in range(a):
		crates[c-1].append(crates[b-1].pop())
	crates2[c-1].extend(crates2[b-1][-a:])
	del crates2[b-1][-a:]
print("".join(c[-1] for c in crates), "".join(c[-1] for c in crates2))
