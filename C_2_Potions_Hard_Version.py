from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain,groupby
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
from heapq import heapify,heappop,heappush,heappushpop,heapreplace
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
n = int(input())
a = list(map(int,input().split()))
negs = []
heapify(negs)
health = 0
ans = 0
for val in a:
    if health+val<0:
        if negs and negs[0]<val:
            health+=val-heappop(negs)
            heappush(negs,val)
    else:
        health+=val
        if val<0:
            heappush(negs,val)
        ans+=1
print(ans)
            
           