import functools as f
F=f.cache(lambda i,j:((F(i*2024,j)if(p:=len(s:=str(i)))%2 else F(int(s[:p//2]),j)+F(int(s[p//2:]),j))if i else F(1,j))if(j:=j-1)else 1)
for i in 26,76:print(sum(F(int(v),i)for v in open("11.in").read().split()))
