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
    n = int(input())
    a = list(map(int,input().split()))
    m = max(a)
    dp = [0]*(m+1) #number of triplets for i+1
    div = defaultdict(list)
    c = [[] for _ in range(m+1)]
    a.sort()
    for i in range(n):
        c[a[i]].append(i)
    for j in range(m+1):
        for k in range(1,m+1):
            if k*j<=m:
                for e in c[k*j]:
                    div[j].append(e)  
            else:
                break
    ans = 0
    for i in reversed(range(1,m+1)):
        triplets = 0
        for ind,ia in enumerate(div[i]):
            triplets+=ind*(n-ia-1)
        st = 2
        while st*i<=m:
            triplets-=dp[st*i]
            st+=1
        dp[i] = triplets
        ans+=triplets*(i)
    print(ans)
            