from functools import lru_cache,cache
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
N = int(1e7) 
mind = [i for i in range(N)]

def precalc():
    for p in range(2, N):
        if mind[p] != p:
            continue
        for d in range(2 * p, N, p):
            mind[d] = min(mind[d], p)

def get_primes(v):
    ps = []
    while v > 1:
        if not ps or ps[-1] != mind[v]:
            ps.append(mind[v])
        v //= mind[v]
    return ps
precalc()
for _ in range(int(input())):
    x,y = map(int,input().split())
    mini = inf
    for d in get_primes(y-x):
        if d!=1:
            r = x%d
            mini = min(mini,(d-r)%d)
    print(mini if mini!=inf else -1)