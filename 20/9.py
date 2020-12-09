ns = [int(x) for x in open("9.in").read().splitlines()]

# Part 1
for i in range(25,len(ns)):
	s = ns[i-25:i]
	b = ns[i]
	has = any(b-w in s for w in s)
	if not has:
		print(b)
		break

# Part 2
n = 0
m = []
for x in ns:
	m.append(x)
	n += x
	while n > b:
		n -= m.pop(0)
	if n == b:
		print(min(m) + max(m))
		break
