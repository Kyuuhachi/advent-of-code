l = [int(x) for x in open("1.in")]

# Part 1: O(n)
s = set(l)
print(*[
	a*b
	for a in s
	if a <= (b := 2020-a) in s
])

# Part 2: O(n²)
s = set(l)
print(*[
	a*b*c
	for a in s
	for b in s
	if a <= b <= (c := 2020-a-b) in s
])
