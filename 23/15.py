inp = open("15.in").read().strip().split(",")

def hash(a) -> int:
	n = 0
	for c in a:
		n = (n + ord(c)) * 17 % 256
	return n

print(sum(hash(a) for a in inp))

boxes = [{} for _ in range(256)]
for a in inp:
	if a.endswith("-"):
		a, () = a.split("-")
		boxes[hash(a)].pop(a, None)
	else:
		[a, b] = a.split("=")
		boxes[hash(a)][a] = int(b)

print(sum(
	i * j * v
	for i, box in enumerate(boxes, 1)
	for j, v in enumerate(box.values(), 1)
))
