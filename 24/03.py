import re
A=B=0
w=1
for a,b,c,d in re.findall(r"mul\((\d+),(\d+)\)|(d)on't\(\)|(d)o\(\)",open("03.in").read()):
 if c+d:w=c<d
 if a:h=int(a)*int(b);A+=h;B+=h*w
print(A,B)
