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
    a = list(map(int,input().split()))
    prefix = [[0 for j in range(n+1)] for k in range(31)]
    
    for i,val in enumerate(a):
        for ind in range(31):
            if (1<<ind)&val:
                prefix[ind][i+1]=prefix[ind][i]+1
    
    def check(l,r,k):
        And = 0
        for ind in range(31):
            if prefix[ind][r]-prefix[ind][l-1] == r-l+1:
                And+=(1<<ind)
        return And>=k
    
    res = []
    for _ in range(int(input())):
        l,k = map(int,input().split())
        if not check(l,l,k):
            res.append(-1)
            continue
        left = l
        right = n
        while left<=right:
            mid = left+(right-left)//2
            if check(l,mid,k):
                ans = mid
                left = mid+1
            else:
                right = mid-1
        res.append(ans)
    print(*res)