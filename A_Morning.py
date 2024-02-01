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
    s = input()
    prev = 1
    res = 4
    for char in s:
        if int(char) == 0:
            res+=abs(10-prev)
            prev = 10
        else:
            res+=abs(int(char)-prev)
            prev = int(char)
    print(res)