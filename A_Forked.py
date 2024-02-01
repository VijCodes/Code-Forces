from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb

#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
for _ in range(int(input())):
    a,b = map(int,input().split())
    xk,yk = map(int,input().split())
    xq,yq = map(int,input().split())
    setK = set()
    setQ = set()
    moves = [(a,-b),(a,b),(-a,-b),(-a,b),(b,a),(b,-a),(-b,-a),(-b,a)]
    for dx,dy in moves:
        setQ.add((xq+dx,yq+dy)) 
        setK.add((xk+dx,yk+dy))
    print(len(setQ.intersection(setK)))  