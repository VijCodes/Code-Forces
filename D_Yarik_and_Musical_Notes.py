from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
 
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
for _ in range(int(input())):
    n = int(input())
    p = list(map(int,input().split()))
    c=Counter()
    res = 0
    for val in p:
        curr = val-log2(val)
        res+=c[curr]
        c[curr]+=1
    print(res)