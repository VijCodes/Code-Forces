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
    n,k,a,b = map(int,input().split())
    points = []
    for i in range(n):
        x,y = map(int,input().split())
        points.append((x,y))
        
    def distance(x1,y1,x2,y2):
        return abs(x1-x2)+ abs(y1-y2)
    # caclulate minimum distance to major city network
    minA,minB = inf,inf
    xA,yA = points[a-1]
    xB,yB = points[b-1]
    for x,y in points[:k]:
        minA = min(minA,distance(x,y,xA,yA))
        minB = min(minB,distance(x,y,xB,yB))
    print(min(minA+minB,distance(xA,yA,xB,yB)))
    
            
        