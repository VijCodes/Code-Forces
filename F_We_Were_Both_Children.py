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

for j in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a = [val for val in a if val<=n]
    c = Counter(a)
    aSet = sorted(list(set(a)))
    #add = c[1]
    res = [0]*(n+1)
    for val in aSet:
        for i in range(val, n + 1, val):
            res[i] += c[val]
    print(max(res))
            
    
    
    