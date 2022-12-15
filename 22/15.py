import re
rx = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?i?\d+), y=(-?\d+)")

# different limits for prod and test
TARGET_LINE = 10
TARGET_LINE = 2000000
SIZE = TARGET_LINE*2+1

inp = []
for line in open("15.in"):
	a,b,c,d = rx.fullmatch(line.strip()).groups()
	inp.append(((int(a),int(b)),(int(c),int(d))))

def _row(n):
	row = []
	for (a,b),(c,d) in inp:
		distToLine = abs(b-n)
		radius = abs(a-c)+abs(b-d)
		if radius >= distToLine:
			row.append((a-(radius-distToLine),a+(radius-distToLine)))
	row.sort()
	return row

row = _row(TARGET_LINE)
end = row[0][0]
n = 0
for a, b in row:
	if b > end:
		n += b-max(end, a)
		end=b
print(n)

for i in range(2630000, 2640000):
	if i % 10000 == 0:
		print(i)
	row = _row(i)
	if row:
		end = 0
		for a, b in row:
			if end < a-1:
				print(i+(a-1)*4000000)
			end = max(b, end)


