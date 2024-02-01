from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

for _ in range(int(input())):
    n,q = map(int, input().split())
    adj = defaultdict(list)
    for _ in range(n-1):
        u,v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    n = list(map(int,input().split()))
    for _ in range(q):
        l,r,x = map(int, input().split())
        