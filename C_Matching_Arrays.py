from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
 
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
for _ in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    sA = sorted(a)
    sB = sorted(b)
    # highest x elements in A to lowest x elements in B. 
    rA = sA[n-x:]+sA[:n-x] 
    rB = sB[:x]+sB[x:]
    #print(rA)
    #print(rB)
    res = True
    mapper = defaultdict(list)
    for i in range(n):
        if i<x:
            if rA[i]<=rB[i]:
                res = False
        else:
            if rA[i]>rB[i]:
                res = False
        mapper[rA[i]].append(rB[i])
    if res:
        ans = [0]*n
        for i in range(n):
            ans[i] = mapper[a[i]].pop()
        print('YES')
        print(' '.join(map(str,ans)))
    else:
        print('NO')
    