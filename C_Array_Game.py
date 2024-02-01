from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb
from sys import stdin
input = lambda: stdin.buffer.readline().decode().strip()
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    if k>2:
        print(0)
    elif k==1:
        a.sort()
        res = a[0]
        for i in range(1,n):
            res = min(a[i]-a[i-1],res)
        print(res)
    else:
        a.sort()
        res = a[0]
        for i in range(1,n):
            res = min(a[i]-a[i-1],res)
        for i in range(n):
            for j in range(i+1,n):
                val = a[j]-a[i]
                high,low = inf,inf
                HighInd = bisect_right(a,val)
                if 0<=HighInd<n:
                    high = a[HighInd]
                LowInd = HighInd-1
                if 0<=LowInd<n:
                    low = a[LowInd]
                res = min(res,abs(low-val),abs(high-val))
        print(res)
                
                
            