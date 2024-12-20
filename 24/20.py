s=open("20.in").read()
p=s.find('S')
M={p:0}
P=0
for x in[-1,w:=s.find('\n')+1,1,-w]*w*w:
 if s<s[p+x]and P+x:P=x;p+=x;M[p]=len(M)

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
