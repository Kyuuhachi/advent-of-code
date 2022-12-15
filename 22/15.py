import re
rx = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?i?\d+), y=(-?\d+)")

# different limits for prod and test
TARGET_LINE = 10
TARGET_LINE = 2000000

inp = []
for line in open("15.in"):
	a,b,c,d = map(int, rx.fullmatch(line.strip()).groups())
	inp.append((a,b,abs(a-c)+abs(b-d)))

row = []
for a,b,r in inp:
	distToLine = abs(b-TARGET_LINE)
	if r >= distToLine:
		row.append((a-(r-distToLine),a+(r-distToLine)))
row.sort()
end = row[0][0]
n = 0
for a, b in row:
	if b > end:
		n += b-max(end, a)
		end=b
print(n)

p1 = {a+b-(r+1) for a,b,r in inp} & {a+b+(r+1) for a,b,r in inp}
p2 = {a-b-(r+1) for a,b,r in inp} & {a-b+(r+1) for a,b,r in inp}
print({
	a*4000000+b
	for q1 in p1 for q2 in p2
	for (a,b) in [((q1+q2)//2, (q1-q2)//2)]
	if all(abs(a-c)+abs(b-d) > r for c,d,r in inp)
})
