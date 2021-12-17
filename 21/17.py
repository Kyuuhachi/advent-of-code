inp = open("17.in").read().removeprefix("target area:").strip()
ix, iy = inp.split(", ")
x0, x1 = map(int, ix.removeprefix("x=").split(".."))
y0, y1 = map(int, iy.removeprefix("y=").split(".."))

assert 0 < x0 < x1
assert y0 < y1 < 0 # this assumption might simplify stuff a little

print(y0*(y0+1)//2)

def hits(dx: int, dy: int) -> bool:
	x = y = 0
	while x <= x1 and y >= y0:
		x += dx
		y += dy
		if dx > 0: dx -= 1
		dy -= 1
		if x0 <= x <= x1 and y0 <= y <= y1:
			return True
	return False

print(sum(
	hits(dx, dy)
	for dy in range(y0,-y0) # if we fire at dy=-y0, we'll end up at {...,0,y0-1}
	for dx in range(0,x1+1)
))
