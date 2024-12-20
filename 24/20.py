s=open("20.in").read()
w=s.find('\n')+1
M={}
p=s.find('S')
d=0
D=1,-1,w,-w
while s[p]!='E':
 for x in D:
  if s[p+x]!='#' and p+x not in M:M[p]=d;p+=x;d+=1
M[p]=d

n=0
k = 0
for a in M:
 k += 1
 if k % 10 == 0:print(k,'/',len(M))
 for b in M:
  d=abs(a%w-b%w)+abs(a//w-b//w)
  if d<=20:
   d=M[a]-M[b]-d
   # if d>=50:print(d)
   if d>=100:n+=1
print(n)
