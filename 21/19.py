import numpy as np
inp = []
for line in open("19.in"):
	line = line.strip()
	if not line:
		continue
	elif line.startswith("---"):
		inp.append([])
	else:
		inp[-1].append(tuple(int(a) for a in line.split(",")))

inp = [np.array(x) for x in inp]

def orient(a):
	for b in [
		a*[[+1,+1,+1]],
		a*[[+1,-1,-1]],
		a*[[-1,-1,+1]],
		a*[[-1,+1,-1]],
	]:
		yield +b[:,[0,1,2]]
		yield +b[:,[1,2,0]]
		yield +b[:,[2,0,1]]
		yield -b[:,[0,2,1]]
		yield -b[:,[2,1,0]]
		yield -b[:,[1,0,2]]

def sort(a):
	return np.array(sorted(a.tolist()))

def align(b, a):
	sb = {tuple(x) for x in b}
	for a in map(sort, orient(a)):
		for ra in a:
			for rb in b:
				sa = {tuple(x) for x in a+rb-ra}
				if len(sa & sb) >= 12:
					return a+rb-ra, rb-ra

inp2 = list(inp)
done = []
done.append(sort(inp2.pop(0)))
for a in done:
	for i, b in reversed(list(enumerate(inp2))):
		match align(a, b):
			case ali, pos:
				print(pos)
				inp2.pop(i)
				done.append(ali)
assert not inp2, inp2

for a in sorted({tuple(a) for b in done for a in b}):
	print(a)
print(len({tuple(a) for b in done for a in b}))
