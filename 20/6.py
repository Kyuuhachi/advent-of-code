polls = [[set(x) for x in a.split()] for a in open("6.in").read().split("\n\n")]

# Part 1
print(sum(len(set.union(*xs)) for xs in polls))

# Part 2
print(sum(len(set.intersection(*xs)) for xs in polls))
