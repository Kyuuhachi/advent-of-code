import functools as F
@F.cache
def G(s,N,B,H):
 if-1==N:return 1
 o=0;A=N-1,' ^A<v>',0
 for c in zip('A'+s,s+'A'):p,P=map(B.find,c);x=P%3-p%3;x='>'*x+'<'*-x;y=P//3-p//3;y='v'*y+'^'*-y;o+=min([G(x+y,*A)][:P%3 or p//3!=H]+[G(y+x,*A)][:p%3 or P//3!=H])
 return o
for N in 3,26:print(sum(int(k:=i[:-2])*G(k,N,'789456123 0A',3)for i in open("21.in")))
