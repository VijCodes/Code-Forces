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
    n,m = map(int,input().split())
    n = n%m 
    
    nReduce = n
    while nReduce and nReduce%2==0:
        nReduce=nReduce//2
        
    mReduce = m
    while mReduce and mReduce%2==0:
        mReduce=mReduce//2
        
    if nReduce%mReduce:
        print(-1)
    else:
        res = 0
        while n:
            res+=n
            n = (2*n)%m
        print(res)
        