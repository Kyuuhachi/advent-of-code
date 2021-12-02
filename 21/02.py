lines = [(a, int(b)) for l in open("02.in") for (a, b) in [l.split()]]

x, y, z = 0, 0, 0
for a, b in lines:
	if a == "forward": x += b; z += y * b
	if a == "up": y -= b
	if a == "down": y += b
print(x*y, x*z)
