s=open("10.in",'rb').read()
w=s.find(10)+1
s+=b'.'*w
R=lambda p,c=48:{}if c-s[p] else R(p-1,c:=c+1)|R(p+1,c)|R(p+w,c)|R(p-w,c)if c-57 else{F(p):0}
A=B=i=0
for c in s:
 F=abs;A+=len(R(i))
 F=property;B+=len(R(i))
 i+=1
print(A,B)
