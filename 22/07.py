root = {}
stack = [root]
for line in open("07.in"):
	line = line.strip();
	if line == "$ cd /":
		stack = [root]
	elif line == "$ cd ..":
		stack.pop()
	elif line.startswith("$ cd "):
		stack.append(stack[-1][line[5:]])
	elif line == "$ ls":
		pass
	else:
		a, b = line.split()
		if a == "dir":
			stack[-1][b] = {}
		else:
			stack[-1][b] = int(a)

sizes = []
def run(node):
	if isinstance(node, int):
		return node
	count = 0
	for v in node.values():
		count += run(v)
	sizes.append(count)
	return count
run(root)

print(sum(a for a in sizes if a <= 1e5))
print(min(a for a in sizes if sizes[-1]-a < 4e7))
