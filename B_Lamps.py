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
    heap = []
    heapify(heap)
    for i in range(n):
        a,b = map(int,input().split())
        heappush(heap,(a,-b))
    xMax,xCurr = 0,0
    score = 0
    dp = [0]*(n+1)
    while heap:
        ai,bi = heappop(heap)
        #print(ai,bi)
        if ai>xMax:
            xCurr+=1
            score-=bi # add score,-ve to counter -b
            dp[ai]+=1
            xMax = max(xMax,xCurr)
            #print(xCurr,xMax)
            #print(dp[xCurr])
            remove = dp[xCurr]
            dp[xCurr]=0
            xCurr-=remove
        #print(dp)
    print(score)                