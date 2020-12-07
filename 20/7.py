import re
spec = {
	k: {
		k: int(n)
		for n, k in re.findall(r"(\d+) ([a-z ]+) bags?", contains)
	}
	for k, contains in re.findall(r"(.+) bags? contain (.+)\.", open("7.in").read())
}

# Part 1
class closure(dict):
	def __missing__(f, key):
		return {key}.union(*(f(k) for k, v in spec.items() if key in v))
print(len(closure()["shiny gold"]) - 1)

# Part 2
class count(dict):
	def __missing__(self, key):
		return 1 + sum(self[k] * n for k, n in spec[key].items())
print(count()["shiny gold"] - 1)
