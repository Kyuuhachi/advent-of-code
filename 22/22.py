import re
import numpy as np
grid, path = open("22.in").read().split("\n\n")

grid = grid.splitlines()
maxw = max(map(len, grid))
grid = np.array([list(a.ljust(maxw, " ")) for a in grid])
grid = np.pad(grid, 1, "constant", constant_values=' ')

path = [a.group() if a.group() in "LR" else int(a.group()) for a in re.finditer(r"\d+|\w", path)]

o = np.full_like(grid, 4, dtype="u8")
(y, x), r = np.argwhere(grid == '.')[0], 0
for a in path:
	o[y, x] = r
	match a:
		case 'L':
			r = (r-1) % 4
		case 'R':
			r = (r+1) % 4
		case int(n):
			dy, dx = [(0,1), (1,0), (0,-1), (-1,0)][r]
			for _ in range(n):
				y0 = (y+dy) % grid.shape[0]
				x0 = (x+dx) % grid.shape[1]
				match grid[y0, x0]:
					case '.':
						y, x = y0, x0
					case '#':
						pass
					case ' ':
						while True:
							y0 = (y0+dy) % grid.shape[0]
							x0 = (x0+dx) % grid.shape[1]
							match grid[y0, x0]:
								case '.':
									y, x = y0, x0
									break
								case '#':
									break
								case ' ':
									continue
				o[y, x] = r
	o[y, x] = r

w = np.zeros_like(grid)
w[grid == ' '] = '░'
w[grid == '.'] = ' '
w[grid == '#'] = '▒'
w[o == 0] = '→'
w[o == 1] = '↓'
w[o == 2] = '←'
w[o == 3] = '↑'
print(w.view(f"U{w.shape[1]}"))
print(y*1000+x*4+r)


# Just hardcoding the maps here. I'm sure there's a clever algorithm for autogenerating them.
if grid[1:-1,1:-1].shape == (12, 16):
	r"""
	Example map:
	   1
	 1/█2
	3███\
	 4\██2
	   43
	"""
	sz = 4
	m = {
		(1,3): (1,3,'\\',1),
		(3,2): (2,0,'-',2),
		(0,1): (0,1,'/',3),
	}
else:
	r"""
	My map:
	  23
	 1██4
	 /█/
	1██4
	2█/
	 3
	"""
	sz = 50
	m = {
		(0,0): (2,-1,'|',2), # 1
		(3,-1): (-1,1,'/',3), # 2
		(4,0): (-1,2,'|',0), # 3
		(2,2): (0,3,'|',2), # 4
		(3,1): (3,1,'/',3),
		(1,2): (1,2,'/',3),
		(1,0): (1,0,'/',3),
	}

for (a,b),(c,d,e,f) in list(m.items()):
	m[c,d] = (a,b,e,f)

def wrap(y, x, r):
	yc,k1 = divmod(y-1,sz)
	xc,k2 = divmod(x-1,sz)
	yc2, xc2, w, r0 = m[yc,xc]
	if w=='\\': y0 = sz-k2; x0 = sz-k1
	if w=='-':  y0 = 1+k1;  x0 = sz-k2
	if w=='/':  y0 = 1+k2;  x0 = 1+k1
	if w=='|':  y0 = sz-k1; x0 = 1+k2
	return yc2*sz+y0, xc2*sz+x0, r^r0

o = np.full_like(grid, 4, dtype="u8")
(y, x), r = np.argwhere(grid == '.')[0], 0
for a in path:
	o[y, x] = r
	match a:
		case 'L':
			r = (r-1) % 4
		case 'R':
			r = (r+1) % 4
		case int(n):
			for _ in range(n):
				dy, dx = [(0,1), (1,0), (0,-1), (-1,0)][r]
				y0 = (y+dy) % grid.shape[0]
				x0 = (x+dx) % grid.shape[1]
				r0 = r
				if grid[y0, x0] == ' ':
					y0, x0, r0 = wrap(y0, x0, r0)
					dy0, dx0 = [(0,1), (1,0), (0,-1), (-1,0)][r0]
					y0 = (y0+dy0) % grid.shape[0]
					x0 = (x0+dx0) % grid.shape[1]
					assert grid[y0,x0] != ' '
				if grid[y0, x0] == '.':
					y, x, r = y0, x0, r0
				o[y, x] = r
	o[y, x] = r

w = np.zeros_like(grid)
w[grid == ' '] = '░'
w[grid == '.'] = ' '
w[grid == '#'] = '▒'
w[o == 0] = '→'
w[o == 1] = '↓'
w[o == 2] = '←'
w[o == 3] = '↑'
print(w.view(f"U{w.shape[1]}"))

print(y*1000+x*4+r)
