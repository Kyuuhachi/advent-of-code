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
	input.append(games)

print(sum(
	i
	for i, games in enumerate(input, 1)
	if all(r <= 12 and g <= 13 and b <= 14 for r, g, b in games)
))
print(sum(
	(
		max(r for r, _, _ in games)
		* max(g for _, g, _ in games)
		* max(b for _, _, b in games)
	) for games in input
))
