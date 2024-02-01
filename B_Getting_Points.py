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
    n,p,l,t = map(int,input().split())
    tasks = (n-1)//7 + 1
    delta = p-t*tasks-l*((tasks+1)//2)
    if delta>0:
        workDays = ceil(tasks/2) + ceil(delta/l)
    else:
        delta2 =  p-t*(tasks//2)*2-l*(tasks//2)
        if delta2>0:
            workDays = ceil(tasks/2)
        else:
            workDays = ceil(p/(2*t+l))
    print(n-workDays)
    