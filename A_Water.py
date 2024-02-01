from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
 
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

for _ in range(int(input())):
    n,Cap = map(int,input().split())
    c = list(map(int,input().split()))
    curr = Cap
    buckets = 1
    for val in c:
        get = min(curr,val)
        curr-=get
        if curr==0:
            buckets+=1
            curr = Cap
    print(buckets)