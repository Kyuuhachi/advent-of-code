import re
inp = []
for line in open("2.in"):
	m = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
	inp.append((int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)))

# Part 1: O(nm) (m = length of strings)
print(len([
	pwd
	for (min,max,ch,pwd) in inp
	if min <= pwd.count(ch) <= max
]))

# Part 2: O(n)
print(len([
	pwd
	for (min,max,ch,pwd) in inp
	if (pwd[min-1] == ch) ^ (pwd[max-1] == ch)
]))
