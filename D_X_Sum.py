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
    for i in range(n):
        grid.append(list(map(int,input().split())))
    pos_diags = defaultdict(int)
    neg_diags = defaultdict(int)
    for i in range(n):
        for j in range(m):
            pos_diags[i-j]+=grid[i][j]
            neg_diags[i+j]+=grid[i][j]
    res = 0
    for i in range(n):
        for j in range(m):
            res = max(res,pos_diags[i-j]+neg_diags[i+j]-grid[i][j])
    print(res)