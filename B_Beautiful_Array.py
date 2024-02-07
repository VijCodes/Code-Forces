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
    n, k, b, s = map(int,input().split())
    if b*k + n*(k-1) >= s >= b*k:
        extra = s - b*k
        div = b//n
        rem = b%n
        res = []
        #print(extra, div, rem)
        for i in range(n):
            multi = div
            if rem:
                rem -= 1
                multi += 1
            add = 0
            if extra:
                add = min(k-1, extra)
                extra -= add
            res.append(multi*k + add)
        print(*res)
    else:
        print(-1)