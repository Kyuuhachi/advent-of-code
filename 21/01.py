inp = [int(x) for x in open("01.in")]
print(sum(a < b for a, b in zip(inp, inp[1:])))
print(sum(a < b for a, b in zip(inp, inp[3:])))
