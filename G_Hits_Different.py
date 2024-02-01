from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain,groupby
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
def sumOfsquare(n):
    return n*(n+1)*(2*n+1)//6
for _ in range(int(input())):
    n = int(input())
    left = 0
    right = 2000
    while left<=right:
        r = left+(right-left)//2
        if r*(r+1)//2 >= n:
            res = r
            right = r-1
        else:
            left = r+1
    r = res
    c = n-(r*(r-1)//2)
    res = 0
    mini,maxi = c,c
    while r:
        if maxi-mini+1==r:
            end = r*(r+1)//2
            res+=end*(end+1)*(2*end+1)//6
            break
        start = r*(r-1)//2 + mini
        end = r*(r-1)//2 + maxi
        res+=sumOfsquare(end)-sumOfsquare(start-1)
        mini,maxi = max(1,mini-1),min(r-1,maxi)
        r-=1
    print(res)