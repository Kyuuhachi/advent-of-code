*s,=map(int,open("11.in").read().split())
import functools as f
F=f.cache(lambda i,j:1 if j==0 else F(1,j-1)if i==0 else F(i*2024,j-1)if(p:=len(s:=str(i)))%2 else F(int(s[:p//2]),j-1)+F(int(s[p//2:]),j-1))
for i in 25,75:print(sum(F(v,i)for v in s))
