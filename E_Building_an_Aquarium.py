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
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    def possible(h):
        return sum([max(0,h-val) for val in a])<=x
    left = 0
    right = x+max(a)+1
    while left<=right:
        mid = left+(right-left)//2
        if possible(mid):
            res = mid
            left = mid+1
        else:
            right = mid-1
    print(res)
    