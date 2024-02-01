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
    n,f,a,b = map(int,input().split())
    m = list(map(int,input().split()))
    dp = [[0,0] for i in range(n+1)] ##off, on
    dp[0][0] = a
    prev = 0
    total = 0
    for i, val in enumerate(m):
        total += min((val-prev)*a,b)
        prev = val
    print('YES' if total<f else 'NO')