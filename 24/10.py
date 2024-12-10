s=open("10.in",'rb').read()
w=s.find(10)+1
def R(p,c):
 if 0<=p<len(s)and s[p]==c:
  if c==57:return{p}
  return R(p-1,c+1)|R(p+1,c+1)|R(p+w,c+1)|R(p-w,c+1)
 return set()

def G(p,c):
 if 0<=p<len(s)and s[p]==c:
  if c==57:return 1
  return G(p-1,c+1)+G(p+1,c+1)+G(p+w,c+1)+G(p-w,c+1)
 return 0
A=B=i=0
for c in s:
 A+=len(R(i,48))
 B+=G(i,48)
 i+=1
print(A,B)
