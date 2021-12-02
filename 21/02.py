lines = [(a, int(b)) for l in open("02.in") for (a, b) in [l.split()]]

x, y = 0, 0
for a, b in lines:
	if a == "forward": x += b
	if a == "up": y -= b
	if a == "down": y += b
print(x*y)

x, y, aim = 0, 0, 0
for a, b in lines:
	if a == "forward": x += b; y += aim * b
	if a == "up": aim -= b
	if a == "down": aim += b
print(x*y)
