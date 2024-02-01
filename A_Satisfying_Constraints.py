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
    q = [-inf,inf]
    seen = []
    for _ in range(n):
        a,x = map(int,input().split())
        if a==1:
            q[0] = max(q[0],x)
        elif a==2:
            q[1] = min(q[1],x)
        else:
            seen.append(x)
    if q[1]>=q[0]:
        res = q[1] - q[0] + 1
        for x in seen:
            if q[0]<=x<=q[1]:
                res-=1
        print(res)
    else:
        print(0)
    
    