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

t, k = map(int,input().split())
dp = [0]*(10**5 + 1)
dp[0] = 1
MOD = 10**9 + 7
for i in range(1, 10**5 + 1):
    dp[i] = (dp[i-1] + (dp[i - k] if i>=k else 0))%MOD
pref_dp = list(accumulate(dp))
for _ in range(t):
    a, b = map(int,input().split())
    print((pref_dp[b] - pref_dp[a-1])%MOD)
    
