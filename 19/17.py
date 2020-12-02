import intcode
import numpy as np
import sys
code = [int(i) for i in sys.stdin.read().split(",")]
ascii = bytes(intcode.intcode(code, [])).splitlines()[:-1]
grid = (np.array([list(x) for x in ascii], "int") != 46).astype("u1")

print(np.dot(*np.where(
	grid
	+np.pad(grid, ((1, 0), (0, 0)))[:-1,:]
	+np.pad(grid, ((0, 1), (0, 0)))[1:,:]
	+np.pad(grid, ((0, 0), (1, 0)))[:,:-1]
	+np.pad(grid, ((0, 0), (0, 1)))[:,1:]
	== 5
)))

# This was just solved by hand, no sophisticated algorithms

# a = """
#                     R,10,L,12,R,6
#                     R,10,L,12,R,6
# R,6,R,10,R,12,R,6,  R,10,L,12,L,12
# R,6,R,10,R,12,R,6,  R,10,L,12,L,12
# R,6,R,10,R,12,R,6,  R,10,L,12,L,12
# R,6,R,10,R,12,R,6,  R,10,L,12,R,6
# """.strip().replace("\n", ",").replace(" ", "")

# p = np.array([14, 0])
# d = np.array([-1, 0])
# grid[tuple(p)] += 1
# for n in a.split(","):
# 	if n == "L": d = d @ [[0,1],[-1,0]]
# 	elif n == "R": d = d @ [[0,-1],[1,0]]
# 	else: p += d * int(n)
# 	grid[tuple(p)] += 1
# np.set_printoptions(edgeitems=100, linewidth=12345)
# print(str(grid).replace("0", "."))

code[0] = 2
intc = intcode.intcode(code, b"A,A,C,B,C,B,C,B,C,A\nR,10,L,12,R,6\nR,10,L,12,L,12\nR,6,R,10,R,12,R,6\nn\n")
print(bytes(intc[:-1]).decode())
print(intc[-1])
