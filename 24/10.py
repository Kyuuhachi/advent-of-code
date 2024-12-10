s=open("10.in",'rb').read()
w=s.find(10)+1
def R(p,c):
 if 0<=p<len(s)and s[p]==c:
  if c==57:return{p}
  return R(p-1,c+1)|R(p+1,c+1)|R(p+w,c+1)|R(p-w,c+1)
 return set()
t=i=0
for c in s:
 t+=len(R(i,48))
 i+=1
print(t)

def R(p,c):
 if 0<=p<len(s)and s[p]==c:
  if c==57:return 1
  return R(p-1,c+1)+R(p+1,c+1)+R(p+w,c+1)+R(p-w,c+1)
 return 0
t=i=0
for c in s:
 t+=R(i,48)
 i+=1
print(t)
