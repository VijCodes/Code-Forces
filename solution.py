from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque,Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
 
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

for _ in range(int(input())):
    n,m = map(int,input().split())
    adds = Counter()
    removals = Counter()
    cEnds = Counter()
    cStarts = Counter()
    segs = set()
    for _ in range(n):
        l,r = map(int,input().split())
        segs.add(l-1)
        segs.add(r-1)
        adds[l-1]+=1
        if r-1<m:
            removals[r-1]+=1
        if r-1==m-1:
            cEnds[l-1]+=1
        if l-1==0:
            cStarts[r-1]+=1
    segs = sorted(list(segs))
    res = 0
    currMax = 0
    start = adds[0]
    end = 0
    for i in segs:
        currMax+=adds[i] 
        end+=cEnds[i]
        res = max(res,currMax-min(end,start))
        start-=cStarts[i]
        currMax-=removals[i]
    print(res)
