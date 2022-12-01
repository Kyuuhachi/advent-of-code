inp = [[]]
for line in open("01.in"):
	if line.strip():
		inp[-1].append(int(line))
	else:
		inp.append([])

print(max(map(sum, inp)))
print(sum(sorted(map(sum, inp))[-3:]))
