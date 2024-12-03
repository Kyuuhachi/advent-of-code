import re
A=B=0
w=1
for a,b,c,d in re.findall(r"mul\((\d+),(\d+)\)|(d)o(n't)?\(\)",open("03.in").read()):
 if c:w=c>d
 if a:h=int(a)*int(b);A+=h;B+=h*w
print(A,B)
