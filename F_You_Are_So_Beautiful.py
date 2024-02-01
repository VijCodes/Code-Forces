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
    a = list(map(int,input().split()))
    
    fIndex,lIndex = {},{}
    
    for i,val in enumerate(a):
        if val not in fIndex:
            fIndex[val]=i
        lIndex[val] = i
        
    res,possLefts = 0,0
    
    for i,val in enumerate(a):
        possLefts+=(fIndex[val]==i)
        res+=(lIndex[val]==i)*(possLefts)
        
    print(res)