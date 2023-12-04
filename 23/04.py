from collections import defaultdict

input = []
for (i, line) in enumerate(open("04.in"), 1):
	a, b = line.split(":")[1].split(" | ")
	a = set(map(int, a.split()))
	b = set(map(int, b.split()))
	input.append(len(a & b))

print(sum(1 << card >> 1 for card in input))

n = 0
q = defaultdict(lambda: 1)
for i, card in enumerate(input):
	n += q[i]
	for j in range(card):
		q[i+1+j] += q[i]
print(n)
