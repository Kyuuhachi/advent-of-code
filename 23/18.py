input1, input2 = [], []
for line in open("18.in"):
	x = line.split()
	input1.append((x[0], int(x[1])))
	input2.append(("RDLU"[int(x[2][-2])], int(x[2][2:-2], 16)))

def run(i):
	n, p, x, y = 0, 0, 0, 0
	for a, b in i:
		py, px = y, x
		p += b
		match a:
			case 'L': x -= b
			case 'R': x += b
			case 'U': y -= b
			case 'D': y += b
		n += (y-py)*(x+px)
	return abs(n)//2 + p//2 + 1

print(run(input1))
print(run(input2))
