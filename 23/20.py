import re
conf = {}
back = {}
for line in open("20.in").read().splitlines():
	kind, name, output = re.match(r"(&|%)?(\w+) -> (.*)", line).groups()
	conf[name] = (kind, output.split(", "))
	for k in output.split(", "):
		back.setdefault(k, []).append(name)

def run(state):
	pulses = [("button", "broadcaster", False)]
	for source, name, s in pulses:
		yield source, name, s
		match conf.get(name):
			case None: pass
			case (None, out):
				pulses.extend((name, o, s) for o in out)
			case ("&", out):
				state[name, source] = s
				s = not all(state.get((name, i)) for i in back[name])
				pulses.extend((name, o, s) for o in out)
			case ("%", out):
				if not s:
					s = not state.get(name)
					state[name] = s
					pulses.extend((name, o, s) for o in out)

count = [0, 0]
state = {}
for v in range(1000):
	for source, name, s in run(state):
		count[s] += 1
print(count[0] * count[1])

[conj] = back["rx"]
assert conf[conj][0] == "&"
goals = set(back[conj])

n = 0
ans = 1
state = {}
while goals:
	n += 1
	for source, name, s in run(state):
		if name in goals and not s:
			ans *= n # could use lcm but eh
			goals.remove(name)
print(ans)
