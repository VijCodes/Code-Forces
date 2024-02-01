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
    starts = defaultdict(list)
    for _ in range(m):
        x,y = map(int,input().split())
        starts[max(x,y)-1].append(min(x,y)-1)
    res = 0
    l = 0
    for r in range(n):
        for st in starts[r]:
            l = max(l,st+1)
        res+=(r-l+1)
    print(res)
    