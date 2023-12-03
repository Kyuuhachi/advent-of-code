import re

input = []
for line in open("03.in"):
	input.append(line.strip())
[width] = {len(line) for line in input}
stride = width + 1
joined = "\n".join(['.' * width, *input, '.' * width])

n = 0
for m in re.finditer(r"\d+", joined):
	near = [joined[m.start() - 1 + s : m.end() + 1 + s] for s in [-stride, 0, stride]]
	near = set("".join(near)) - set('0123456789.\n')
	if near:
		n += int(m.group())
print(n)

numbers = {}
for m in re.finditer(r"\d+", joined):
	for i in range(m.start(), m.end()):
		numbers[i] = (m.start(), int(m.group()))

n = 0
for i, ch in enumerate(joined):
	if ch != '*': continue
	nearby = {
		numbers[i + s]
		for s in [-stride-1, -stride, -stride+1, -1, 1, stride-1, stride, stride+1]
		if i+s in numbers
	}
	if len(nearby) == 2:
		[[_, a], [_, b]] = nearby
		n += a * b
print(n)
