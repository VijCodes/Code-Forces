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
for _ in range(int(input())):
    n = int(input())
    c = Counter()
    for _ in range(n-1):
        u,v = map(int,input().split())
        c[u]+=1
        c[v]+=1
    leaves = 0
    for vert,cnt in c.items():
        if cnt==1:
            leaves+=1
    print(ceil(leaves/2))