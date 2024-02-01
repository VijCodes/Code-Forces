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
    countV = Counter()
    countH = Counter()
    countP = Counter() # +ve slope
    countN = Counter() # -ve slope
    res = 0
    for _ in range(n):
        x,y = map(int,input().split())
        # Add matches over vertical line
        res+=countV[x]
        countV[x]+=1
        # Add matches over horizantal line
        res+=countH[y]
        countH[y]+=1
        # Add matches over +ve slope
        #x-y = k
        res+=countP[x-y]
        countP[x-y]+=1
        # Add matches over -ve slope
        res+=countN[x+y]
        countN[x+y]+=1
    print(res*2)
    