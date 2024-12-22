import functools as F
s=open("21.in").read().split()

@F.cache
def G(s,N,board):
 if N==0:return len(s)
 out=0
 pos=board.find('A')
 hole = board.find(' ')
 for c in s:
  npos=board.find(c)
  dx=npos%3-pos%3;   dx='>'*dx+'<'*-dx
  dy=npos//3-pos//3; dy='v'*dy+'^'*-dy
  k=[]
  if npos%3!=hole%3 or pos//3!=hole//3:k+=[g(dx+dy+'A',N-1)]
  if pos%3!=hole%3 or npos//3!=hole//3:k+=[g(dy+dx+'A',N-1)]
  out+=min(k)
  pos=npos
 return out
NUMPAD = '789456123 0A'
DIRPAD = ' ^A<v>'

f=lambda*a:G(*a,NUMPAD)
g=lambda*a:G(*a,DIRPAD)

n=0
w="""
<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A
<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A
<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
""".split()

def run(s, board):
 y,x=divmod(board.find('A'),3)
 o=""
 for c in s:
  if c=='<':x-=1
  if c=='>':x+=1
  if c=='^':y-=1
  if c=='v':y+=1
  if c=='A':o+=board[y*3+x]
  assert 0<=x<3 and 0<=y<4, (x,y)
  assert board[y*3+x]!=' '
 return o

for i,w in zip(s,w):
 a = f(i, 26)
 print(i, a)
 # print('....', len(w), w)
 # print(run(w,DIRPAD))
 # print(run(run(w,DIRPAD),DIRPAD))
 # print(run(run(run(w,DIRPAD),DIRPAD),NUMPAD))
 # print(i)
 # print()
 n+=int(i[:-1])*(a)
print(n)

# 185776 too low
