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
    w = list(map(int,input().split()))
    acc = set()
    pre =set(accumulate(w))
    suf = set(accumulate(w[::-1]))
    valToInd = defaultdict(int)
    for j,val in enumerate(list(accumulate(w[::-1]))):
        valToInd[val]=j
    summ = 0
    res = 0
    total = sum(w)
    for i in range(n):
        summ+=w[i]
        if summ>total//2:
            break
        if summ in suf:
            res = max(res,valToInd[summ]+1+i+1)
    print(res)
    