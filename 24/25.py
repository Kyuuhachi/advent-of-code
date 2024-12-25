K=[]
for s in open("25.in").read().split("\n\n"):
 g=0
 for i,p in enumerate(s):g|=(p=='#')<<i
 K+=[g]
print(sum(a>b and not a&b for a in K for b in K))
