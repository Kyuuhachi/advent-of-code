import numpy as np
for L in open(n:=0):
 P,*Q,R=L.split()
 A=np.array([*P][1:-1])<'.'
 C=np.array(eval(R[1:-1]+","))
 B=np.zeros((len(Q),len(C)))
 for q,b in zip(Q,B):b[[*eval(q[1:-1]+",")]]=1
 m=np.arange(1<<len(B))[:,None]>>np.arange(len(B))&1
 n+=m[(m@B%2==A).all(axis=1)].sum(axis=1).min()
print(n)
