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
    segs = []
    for _ in range(n):
        l,r = map(int,input().split())
        segs.append((l,r))
    def check(k):
        oldl,oldr = -k,k
        for l,r in segs:
            if l>oldr or r<oldl:
                return False
            oldl,oldr = max(l,oldl)-k,min(r,oldr)+k
        return True
    left = 0
    right = 10**9+1
    while left<=right:
        mid = left+(right-left)//2
        if check(mid):
            res = mid
            right = mid-1
        else:
            left = mid+1
    print(res)