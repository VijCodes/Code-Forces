from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb
from sys import stdin,stdout
input = lambda: stdin.buffer.readline().decode().strip()
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
def check(time):
    l,r = -inf,inf
    for i in range(n):
        l1,r1 = x[i]-(time-t[i]),x[i]+(time-t[i])
        if l1>r or r1<l:
            return inf
        l,r = max(l1,l),min(r1,r)
    return (l+r)/2
    
for _ in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))
    t = list(map(int,input().split()))
    l = max(t)
    r = 10**9
    delta = 10**(-7)
    while r-l>delta:
        mid = l+(r-l)/2
        ans = check(mid)
        if  ans == inf:
            l = mid+delta
        else:
            res = ans
            r = mid-delta
    print(res)