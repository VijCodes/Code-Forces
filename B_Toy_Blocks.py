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
    n = int(input())
    a = list(map(int,input().split()))
    mini = min(a)
    maxi = max(a)
    deficit = sum([maxi-val for val in a])-(maxi-mini)
    res = (deficit-mini)
    if res<0:
        k = ceil(-res/(n-1))
        res += (n-1)*k
    print(res)