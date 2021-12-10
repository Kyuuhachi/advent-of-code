lines = [a.strip() for a in open("10.in")]

close = {
	"(": ")",
	"[": "]",
	"{": "}",
	"<": ">",
}

score_a = {
	")": 3,
	"]": 57,
	"}": 1197,
	">": 25137,
}

score_b = {
	")": 1,
	"]": 2,
	"}": 3,
	">": 4,
}

a = 0
b = []
for l in lines:
	stack: list[str] = []
	for c in l:
		if [c] == stack[-1:]:
			stack.pop()
		elif c in close:
			stack.append(close[c])
		else:
			a += score_a[c]
			break
	else:
		s = 0
		for c in stack[::-1]:
			s = s * 5 + score_b[c]
		b.append(s)
print(a)
print(sorted(b)[len(b)//2])
