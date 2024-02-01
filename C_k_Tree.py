from functools import lru_cache, cache
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


n, k, d = map(int,input().split())
MOD = 10**9 + 7

@cache 
def count_combs(n, d_ind = False):
    if n == 0:
        return int(d_ind)
    res = 0
    for i in range(1, min(n, k)+1):
        res = (res + count_combs(n - i, d_ind or (i >= d))) % MOD
    return res

print(count_combs(n))
            