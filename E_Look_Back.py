from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,ceil
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ops = 0
    prev = a[0]
    carry = 0
    for val in a[1:]:
        lg = 0
        val1 = val
        if prev>val:
            while prev>val:
                lg+=1
                val*=2
        elif prev<val:
            while prev<val and carry+lg>0:
                lg-=1
                prev*=2
            if prev>val:
                lg+=1
        carry+=lg
        ops+=carry
        prev = val1
    print(ops)