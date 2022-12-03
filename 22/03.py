input = open("03.in").read().splitlines()
value = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

score = 0
for line in input:
	a, b = line[:len(line)//2], line[len(line)//2:]
	[x] = set(a) & set(b)
	score += value.find(x)
print(score)

score = 0
it = iter(input)
for a, b, c in zip(it, it, it):
	[x] = set(a) & set(b) & set(c)
	score += value.find(x)
print(score)
