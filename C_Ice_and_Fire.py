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
    s = input()
    res = []
    past = -1
    cons = 0
    x = 2
    for chr in s:
        if chr!=past:
            cons = 0
        cons+=1
        res.append(x-cons)
        past = chr
        x+=1
    print(' '.join(map(str,res)))
        