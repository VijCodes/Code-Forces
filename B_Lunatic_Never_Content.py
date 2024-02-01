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
    for i in range(n//2):
        if i==0:
            res = abs(a[i]-a[n-i-1])
        else:
            res = gcd(res,a[i]-a[n-i-1])
    if n==1:
        res = 0
    print(res)
            