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

for j in range(int(input())):
    grid = []
    for k in range(8):
        grid.append(input())
    #print(grid)
    start = 0
    for r in range(8):
        for c in range(8):
            if grid[r][c]!='.':
                start = (r,c)
                break
        if start:
            break
    res = ''
    row,col = r,c
    for row in range(r,8):
        if grid[row][c]=='.':
            break
        res+=grid[row][c]
    print(res)