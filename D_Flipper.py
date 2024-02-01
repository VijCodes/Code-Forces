from copy import deepcopy
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
    n = int(input())
    p = list(map(int,input().split()))
    if n==1:
        print(*p)
        continue
    maxInd = p.index(n)
    def operation(l,r):
        ans = deepcopy(p[r+1:]+p[l:r+1][::-1]+p[:l])
        return ans
    if maxInd==0:
        maxInd = p.index(n-1)
    res = operation(maxInd,maxInd)
    res = max(res,operation(0,maxInd))
    r = maxInd-1
    for l in range(r+1):
        res = max(res,operation(l,r))
    print(*res)