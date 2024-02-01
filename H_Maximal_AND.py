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
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    count = defaultdict(int)
    for val in a:
        for j in range(31):
            if (1<<j)&val==0:
                count[j]+=1
    res = 0
    for ind in reversed(range(31)):
        if k>=count[ind]:
            res+=(1<<ind)
            k-=count[ind]
    print(res)