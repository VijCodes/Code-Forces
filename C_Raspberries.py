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
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    ops = inf
    for val in a:
        if val%k==0:
            ops = 0
            break
        ops = min(k-(val%k),ops)
    if k==4 and ops:
        evens = sum([val%2==0 for val in a])
        if evens>=2:
            ops = 0
        elif evens==0:
            ops = min(2,ops)
        else:
            ops = 1
    print(ops)