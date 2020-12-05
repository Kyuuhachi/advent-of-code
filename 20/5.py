tr = str.maketrans("FBLR", "0101")
ns = {int(x.translate(tr), 2) for x in open("5.in").read().splitlines()}

# Part 1
print(max(ns))

# Part 2
print({x-1 for x in ns} & {x+1 for x in ns} - ns)
