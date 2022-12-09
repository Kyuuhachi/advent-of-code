inp = open("09.in").read().splitlines()
x = [0]*10
y = [0]*10
seen1 = {(0, 0)}
seen2 = {(0, 0)}

d = [
	[-1, 0, 0, 0,-1],
	[-1,-1, 0,+1,+1],
	[-1,-1, 0,+1,+1],
	[-1,-1, 0,+1,+1],
	[-1, 0, 0, 0,+1],
]

for l in inp:
	for _ in range(int(l[2:])):
		match l[0]:
			case "U": y[0] += 1
			case "L": x[0] -= 1
			case "R": x[0] += 1
			case "D": y[0] -= 1

		for i in range(1, 10):
			dx = x[i]-x[i-1]
			dy = y[i]-y[i-1]
			x[i] = x[i-1] + d[dy+2][dx+2]
			x[i] = y[i-1] + d[dx+2][dy+2]

		seen1.add((x[1], y[1]))
		seen2.add((x[9], y[9]))

# 		for a in reversed(range(min(b for a,b in seen1), max(b for a,b in seen1)+1)):
# 			for b in range(min(a for a,b in seen1), max(a for a,b in seen1)+1):
# 				for i in range(10):
# 					if (b,a) ==(x[i],y[i]):
# 						print(i, end="")
# 						break
# 				else:
# 					print(".", end="")
# 			print("")
# 		print()

print(len(seen1))
print(len(seen2))

# for a in reversed(range(min(b for a,b in seen2), max(b for a,b in seen2)+1)):
# 	for b in range(min(a for a,b in seen2), max(a for a,b in seen2)+1):
# 		if (b,a) in seen2:
# 			print("#", end="")
# 		else:
# 			print(".", end="")
# 	print("")
