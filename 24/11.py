*s,=map(int,open("11.in").read().split())
import functools as f
@f.cache
def F(i,j):
 if j == 0:return 1
 if i == 0:return F(1,j-1)
 if(p:=len(s:=str(i)))%2:return F(i*2024,j-1)
 return F(int(s[:p//2]),j-1)+F(int(s[p//2:]),j-1)
print(sum(F(v,25)for v in s))
print(sum(F(v,75)for v in s))
