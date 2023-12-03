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

def get_number(pos) -> tuple[int, int]:
	end = pos
	while joined[pos-1] in "0123456789":
		pos -= 1
	while joined[end] in "0123456789":
		end += 1
	return (pos, int(joined[pos:end]))

n = 0
for i, ch in enumerate(joined):
	if ch != '*': continue
	nearby = {
		get_number(i + s)
		for s in [-stride-1, -stride, -stride+1, -1, 1, stride-1, stride, stride+1]
		if joined[i+s] in "0123456789"
	}
	if len(nearby) == 2:
		[[_, a], [_, b]] = nearby
		n += a * b
print(n)
