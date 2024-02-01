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
    x, n = map(int,input().split())
    divisors = []
    for pos in range(1,int(sqrt(x))+1):
        if x%pos == 0:
            divisors.append(pos)
            if pos**2 != x:
                divisors.append(x//pos)
    res = 1
    for d in divisors:
        if x//d >= n:
            res = max(res, d)
    print(res)