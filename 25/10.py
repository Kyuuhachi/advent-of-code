for L in open(n:=0):
 A,*B,C=L.split()
 A=sum(1<<i-1 for i,c in enumerate(A)if c=='#')
 B=[sum(1<<n for n in eval(x.replace(*"({").replace(*")}")))for x in B]
 print(len(B))
 w=1e9
 for b in range(1<<len(B)):
  d=0
  for i in range(len(B)):
   if b>>i&1:d^=B[i]
  if d==A:w=min(w,b.bit_count())
 print(w)
 n+=w
print(n)
