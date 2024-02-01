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


n,k = map(int,input().split())
a = list(map(int,input().split()))
first = -1
last = -1
for i,val in enumerate(a):
    if val>k and first==-1:
        first = i
        last = i
    elif val>k:
        last = i
if first==-1:
    print(n)
elif last==first:
    print(n-1)
else:
    print(first+n-last-1)