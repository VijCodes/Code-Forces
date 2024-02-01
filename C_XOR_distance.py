from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb,ceil,floor
from sys import stdin,stdout
input = lambda: stdin.buffer.readline().decode().strip()
from heapq import heapify,heappop,heappush,heapreplace
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

for _ in range(int(input())):
    a, b, r = map(int,input().split())
    a, b = sorted([a, b])
    diff = a^b
    mod_r = 0
    change = False
    for i in reversed(range(64)):
        if (1 << i)&diff and not change:
            change = True
        elif (1<<i)&diff and change and (1<<i)&b and r>=(1<<i):
            r -= (1<<i)
            mod_r |= (1<<i)
    print(abs((a^mod_r) - (b^mod_r)))

    