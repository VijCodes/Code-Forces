# **** Packages **** #
 
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
    lower = inf
    higher = inf
    res = 0
    for val in p:
        if val>lower and val<higher:
            res+=1
            higher = min(val,higher)
        else:
            lower = min(val,lower)      
    print(res)
