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
    a = list(map(int,input().split()))
    mi = min(a)
    res = 0
    for val in a:
        delta = val-mi
        if delta:
            res = max(res,int(log2(delta))+1)
    ans = [mi]*res
    print(res)
    if 1<=res<=n:
        print(' '.join(map(str,ans)))