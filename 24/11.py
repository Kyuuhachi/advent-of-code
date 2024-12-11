import functools as f
F=f.cache(lambda i,j:((F(i*2024,j-1)if(p:=len(s:=str(i)))%2 else F(int(s[:p//2]),j-1)+F(int(s[p//2:]),j-1))if i else F(1,j-1))if j else 1)
for i in 25,75:print(sum(F(int(v),i)for v in open("11.in").read().split()))
