import re

numbers = {str(n): n for n in range(10)}
rx = re.compile("(?=(%s))" % "|".join(numbers))
n = 0
for line in open("01.in"):
	x = [numbers[x.group(1)] for x in rx.finditer(line)]
	n += x[0]*10 + x[-1]
print(n)

numbers |= {
	"zero": 0,
	"one": 1,
	"two": 2,
	"three": 3,
	"four": 4,
	"five": 5,
	"six": 6,
	"seven": 7,
	"eight": 8,
	"nine": 9,
}
rx = re.compile("(?=(%s))" % "|".join(numbers))
n = 0
for line in open("01.in"):
	x = [numbers[x.group(1)] for x in rx.finditer(line)]
	n += x[0]*10 + x[-1]
print(n)
