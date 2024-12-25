K=[sum((p=='#')<<i for i,p in enumerate(s))for s in open("25.in").read().split("\n\n")]
print(sum((a>b)&(a&b==0)for a in K for b in K))
