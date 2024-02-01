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
    a = list(map(int,input().split()))
    last = defaultdict(int)
    for i,val in enumerate(a):
        last[val]=i
    suff = list(accumulate(a[::-1]))[::-1]+[0]
    res = sum(a)
    for i,val in enumerate(a):
        if  suff[i+1]>0:
            res+=suff[i+1]
    print(res)