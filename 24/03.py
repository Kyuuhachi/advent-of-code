import re
A=B=w=0
for a,b,d in re.findall(r"mul\((\d+),(\d+)\)|do(n't)?\(\)",open("03.in").read()):
 if a:h=int(a)*int(b);A+=h;B+=h-h*w
 else:w=a<d
print(A,B)
