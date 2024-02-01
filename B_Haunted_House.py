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
    s = input()
    res = []
    zerosIndex = []
    for i in range(n):
        if s[i]=='0':
            zerosIndex.append(n-i-1)
    filled = 0
    Swaps = 0
    for i in range(1,n+1):
        if not zerosIndex:
            res.append(-1)
        else:
            currInd = zerosIndex.pop()
            Swaps += currInd-filled
            filled+=1
            res.append(Swaps)
    print(*res)