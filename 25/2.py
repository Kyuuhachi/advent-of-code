S={n:=0}
for L in open(0).read().split(','):
 A,B=map(int,L.split('-'))
 for i in 2,3,5,7:
  t={(j:=int(str(J)*i))*(A<=j<=B)for J in range(int(B**(1/i)))}
  n+=sum(t)*(i==2)
  S|=t
print(n,sum(S))
