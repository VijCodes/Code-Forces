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
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    acts = [[a[i],b[i],c[i]] for i in range(n)]
    dp = [-inf]*8 #
    dp[0] = 0
    for i in range(n):
        newDp = dp[:]
        for j in range(8):
            for k in range(3):
                if (1<<k)&j:
                    newDp[j] = max(newDp[j],dp[j^(1<<k)]+acts[i][k])
        dp = newDp
    print(max(dp))
    