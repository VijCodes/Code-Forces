from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split)))
# int(input())

for _ in range(int(input())):
    n = input()
    res = 1
    for char in n:
        d = int(char)
        res*=comb(d+2,2)
    print(res)
    