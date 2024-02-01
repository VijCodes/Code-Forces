from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb,ceil,floor
from sys import stdin,stdout
input = lambda: stdin.buffer.readline().decode().strip()

#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
MOD = 998244353
for i in range(int(input())):
    a,b,x,y,n = map(int,input().split())
    res = inf
    ### remove a first
    rem = min(a-x,n)
    remSteps = n-rem
    rem2 = min(b-y,remSteps)
    res = min(res,(a-rem)*(b-rem2))
    ### remove a first
    rem = min(b-y,n)
    remSteps = n-rem
    rem2 = min(a-x,remSteps)
    res = min(res,(b-rem)*(a-rem2))
    print(res)