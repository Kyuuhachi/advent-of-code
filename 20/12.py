import cmath as math
xs = [(x[0], int(x[1:])) for x in open("12.in").read().splitlines()]

p = 0
f = 1
for d, v in xs:
	if d == "E": p += v
	if d == "N": p += v*1j
	if d == "W": p += v*-1
	if d == "S": p += v*-1j
	if d == "L": f *= math.exp(v/180*math.pi*1j)
	if d == "R": f *= math.exp(v/180*math.pi*-1j)
	if d == "F": p += f*v
print(round(abs(p.real)+abs(p.imag)))

p = 0
f = 10+1j
for d, v in xs:
	if d == "E": f += v
	if d == "N": f += v*1j
	if d == "W": f += v*-1
	if d == "S": f += v*-1j
	if d == "L": f *= math.exp(v/180*math.pi*1j)
	if d == "R": f *= math.exp(v/180*math.pi*-1j)
	if d == "F": p += f*v
print(round(abs(p.real)+abs(p.imag)))
