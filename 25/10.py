for L in open(n:=0):
 A,*B,C=L.split()
 A={i-1 for i,c in enumerate(A)if c=='#'}
 B=[{int(n)for n in x[1:-1].split(",")}for x in B]
 C=[int(n)for n in C[1:-1].split(",")]
 print(A,B,C)
 w=1e9
 for b in range(1<<len(B)):
  d=A^A
  for i in range(len(B)):
   if b>>i&1:d^=B[i]
  if d==A:w=min(w,b.bit_count())
 print(w)
 n+=w
print(n)
