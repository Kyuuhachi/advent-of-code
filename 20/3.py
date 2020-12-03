field = open("3.in").read().splitlines()

# Part 1: O(n)
def count(x, y):
	pos = 0
	n = 0
	for line in field[::y]:
		n += line[pos] == "#"
		pos = (pos + x) % len(line)
	return n
print(count(3, 1))

# Part 2: O(n)
print(count(1, 1) * count(3, 1) * count(5, 1) * count(7, 1) * count(1, 2))
