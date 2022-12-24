import dataclasses as dc
import re
from math import prod
rx = re.compile(r"Blueprint (\d+): Each ore robot costs (\d+) ore\. Each clay robot costs (\d+) ore\. Each obsidian robot costs (\d+) ore and (\d+) clay\. Each geode robot costs (\d+) ore and (\d+) obsidian\.")

@dc.dataclass(frozen=True)
class Bp:
	num: int
	ore_ore: int
	clay_ore: int
	obs_ore: int
	obs_clay: int
	geo_ore: int
	geo_obs: int

bp = []
for line in open("19.in"):
	bp.append(Bp(*map(int, rx.fullmatch(line.strip()).groups())))

def run(bp: Bp, t: int):
	q = [(t,(1,0,0,0),(0,0,0,0))]
	mx = 0
	tested, pruned = 0, 0
	while q:
		t, (A,B,C,D), (a,b,c,d) = q.pop()
		if d+sum(D+k for k in range(t)) <= mx:
			pruned += 1
			continue
		tested += 1
		mx = max(mx, d+D*t)
		if A < 4:
			dt = 1+max([
				0,
				-(-(bp.ore_ore-a)//A),
			])
			if dt <= t:
				q.append((t-dt, (A+1,B,C,D), (a+A*dt-bp.ore_ore, b+B*dt, c+C*dt, d+D*dt)))
		if A:
			dt = 1+max([
				0,
				-(-(bp.clay_ore-a)//A),
			])
			if dt <= t:
				q.append((t-dt, (A,B+1,C,D), (a+A*dt-bp.clay_ore, b+B*dt, c+C*dt, d+D*dt)))
		if A and B:
			dt = 1+max([
				0,
				-(-(bp.obs_ore-a)//A),
				-(-(bp.obs_clay-b)//B),
			])
			if dt <= t:
				q.append((t-dt, (A,B,C+1,D), (a+A*dt-bp.obs_ore, b+B*dt-bp.obs_clay, c+C*dt, d+D*dt)))
		if A and C:
			dt = 1+max([
				0,
				-(-(bp.geo_ore-a)//A),
				-(-(bp.geo_obs-c)//C),
			])
			if dt <= t:
				q.append((t-dt, (A,B,C,D+1), (a+A*dt-bp.geo_ore, b+B*dt, c+C*dt-bp.geo_obs, d+D*dt)))
	print(f"{bp.num} max={mx}, {tested=}, {pruned=}")
	return mx

print(sum(b.num * run(b, 24) for b in bp))
print(prod(run(b, 32) for b in bp[:3]))
