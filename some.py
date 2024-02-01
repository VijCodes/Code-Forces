
from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter

n,q  = map(int,input().split())
positions = [(i+1,0) for i in range(n)]
for _ in range(q):
  ind,point  = map(str,input().split())
  if ind=='1':
    positions.pop()
    x,y = positions[0]
    if point == 'U':
      nx,ny = x,y+1
      positions.appendleft((nx,ny))
    if point == 'D':
      nx,ny = x,y-1
      positions.appendleft((nx,ny))
    if point == 'L':
      nx,ny = x-1,y
      positions.appendleft((nx,ny))
    if point == 'R':
      nx,ny = x+1,y
      positions.appendleft((nx,ny))
  else:
    print(positions[int(point)-1])
    