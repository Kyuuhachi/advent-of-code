inp = open("10.in").read().splitlines()

def gen():
	n = 1
	for line in inp:
		match line.split():
			case ["noop"]:
				yield n
			case ["addx", m]:
				m = int(m)
				yield n
				yield n
				n += m

tot = 0
screen = ""
for i, a in enumerate(gen()):
	if i % 40 == 19:
		tot += (i+1) * a
	screen += "█" if -1 <= a-i%40 <= 1 else "░"
	if i % 40 == 39:
		print(screen)
		screen = ""
# We print task 2 before task 1 today
print(tot)
