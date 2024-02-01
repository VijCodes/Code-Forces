from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
 
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

MOD = 998244353
for _ in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    prev = 0
    res = 0
    for val in a+[x+x-a[-1]]:
        res = max(res,val-prev)
        prev = val
    print(res)