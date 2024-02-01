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
        grid.append(list(map(int,input().split())))
    def minPath(i,j,value):
        if i<0 or i>=n or j<0 or j>=m:
            return inf
        if grid[i][j]<value:
            return inf
        if i==n-1 and j==m-1:
            return grid[i][j]-value
        return min(minPath(i,j+1,value+1),minPath(i+1,j,value+1))+grid[i][j]-value
    res = inf
    for r in range(n):
        for c in range(m):
            value = grid[r][c]-(r+c)
            res = min(res,minPath(0,0,value))
    print(res)
        