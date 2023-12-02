import numpy as np

input = []
for (i, line) in enumerate(open("02.in"), 1):
	assert line.startswith(f"Game {i}: ")
	games = []
	for part in line.removeprefix(f"Game {i}: ").strip().split("; "):
		red = green = blue = "0"
		for count in part.split(", "):
			match count.split():
				case [red, "red"]: pass
				case [green, "green"]: pass
				case [blue, "blue"]: pass
				case _: raise ValueError(count)
		games.append((int(red), int(green), int(blue)))
	input.append(np.array(games))

print(sum(i for i, games in enumerate(input, 1) if np.all(games <= [12, 13, 14])))
print(sum(games.max(axis=0).prod() for games in input))
