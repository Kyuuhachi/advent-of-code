s=open("16.in").read()

G=[2*[-2 if c=='#' else 1e9]for c in s]
w = s.find('\n')+1
step = [1,w]

def advance(p, d, g, j):
 while G[p][d] > g:
  G[p][d] = g
  F.append((p, 1-d, g+1000))
  p += step[d] * j
  g += 1

F=[(s.find('S'), 0, 1)]
for p, d, g in F:
 t = G[p][d] # ugly workaround to keep state
 advance(p, d, g, -1)
 G[p][d] = t
 advance(p, d, g, 1)

e = s.find('E')
P = [(e, G[e][0] > G[e][1])]
for p, d in P:
 if G[p][1-d] == G[p][d]-1000: P.append((p, 1-d))
 for k in [-step[d], step[d]]:
  if G[p+k][d] == G[p][d]-1: P.append((p+k, d))

print(min(G[e]), len({a for a,b in P}))

# for i,c in enumerate(s):
#  def I(i, j):
#   if (i, j) in P: return '\x1B\x5B48;5;9m'
#   return ''
#  print(f"{I(i,0)}{G[i][0]:5}\x1B\x5Bm", end=',')
#  print(f"{I(i,1)}{G[i][1]:5}\x1B\x5Bm", end=' ')
#  if c == '\n': print()
