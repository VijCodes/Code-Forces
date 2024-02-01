from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain,groupby
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
def FindVolume(x1,y1):
    search = [(x1,y1)]
    Volume = 0
    while search:
        x,y = search.pop()
        Volume+=grid[x][y]
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<rows and 0<=ny<cols and (nx,ny) not in seen and grid[nx][ny]>0:
                seen.add((nx,ny))
                search.append((nx,ny))
    return Volume
for _ in range(int(input())):
    rows,cols = map(int,input().split())
    grid = []
    for _ in range(rows):
        grid.append(list(map(int,input().split())))
    seen = set()
    res = 0
    for r in range(rows):
        for c in range(cols):
            if (r,c) not in seen and grid[r][c]>0:
                seen.add((r,c))
                vol = FindVolume(r,c)
                res = max(res,vol)
    print(res)
    