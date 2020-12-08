insns = [
	(a, int(b))
	for a, b in (l.split() for l in open("8.in").read().splitlines())
]

def run(code, i=0, acc=0, seen=None):
	if seen is None: seen = set()
	while i < len(code) and i not in seen:
		seen.add(i)
		a, b = code[i]
		if a == "acc":
			acc += b
			i += 1
		elif a == "jmp":
			i += b
		elif a == "nop":
			i += 1
	return acc, i

# Part 1
print(run(insns)[0])

# Part 2
for i in range(len(insns)):
	insns2 = list(insns)
	if insns2[i][0] == "nop":
		insns2[i] = ("jmp", insns2[i][1])
	elif insns2[i][0] == "jmp":
		insns2[i] = ("nop", insns2[i][1])
	else:
		continue
	a, b = run(insns2)
	if b >= len(insns2):
		print(a)
