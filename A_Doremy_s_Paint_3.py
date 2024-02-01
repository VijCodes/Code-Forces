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
    c=Counter(a)
    if len(c)==1:
        print('Yes')
    elif len(c)==2:
        f,s = c.values()
        if abs(f-s)<=1:
            print('Yes')
        else:
            print('No')
    else:
        print('No')