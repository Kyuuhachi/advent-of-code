S={n:=0}
for L in open(0).read().split(','):
 A,B=map(int,L.split('-'))
 for i in 2,3,5,7:
  for j in range(int(B**(1/i))):
   j=int(str(j)*i)
   j*=A<=j<=B
   n+=j*(i==2)
   S|={j}
print(n,sum(S))
