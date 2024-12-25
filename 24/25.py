K=[]
for s in open("25.in").read().split("\n\n"):
 g=0
 for i,p in enumerate(s):
  if p=='#':g|=1<<i
 K+=[g]
print(sum(a>b and not a&b for a in K for b in K))
