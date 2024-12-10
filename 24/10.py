s=open("10.in",'rb').read()
w=s.find(10)+1
def R(p,c):
 if 0<=p<len(s)and s[p]==c:
  if c==57:return{F(p)}
  return R(p-1,c:=c+1)|R(p+1,c)|R(p+w,c)|R(p-w,c)
 return set()
A=B=i=0
for c in s:
 F=abs;A+=len(R(i,48))
 F=property;B+=len(R(i,48))
 i+=1
print(A,B)
