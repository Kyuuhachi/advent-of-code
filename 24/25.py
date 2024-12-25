K=[]
for s in open("25.in").read().split("\n\n"):
 K+=[sum((p=='#')<<i for i,p in enumerate(s))]
print(sum(a>b and not a&b for a in K for b in K))
