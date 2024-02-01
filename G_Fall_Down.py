from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb,ceil,floor
from sys import stdin,stdout
input = lambda: stdin.buffer.readline().decode().strip()
from heapq import heapify,heappop,heappush,heapreplace
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

for _ in range(int(input())):
    n,m = map(int,input().split())
    grid = []
    for _ in range(n):
        grid.append(list(input()))
    obsIndex = defaultdict(lambda:n) # columns obs index
    for r in reversed(range(n)):
        for c in range(m):
            if grid[r][c]=='*':
                grid[r][c],grid[obsIndex[c]-1][c] = grid[obsIndex[c]-1][c],grid[r][c]
                obsIndex[c]-=1
            elif grid[r][c]=='o':
                obsIndex[c]=r
    for lst in grid:
        print(''.join(lst))
    