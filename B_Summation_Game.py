from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb,ceil,floor
from sys import stdin
input = lambda: stdin.buffer.readline().decode().strip()
from heapq import heapify,heappop,heappush,heapreplace
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

for _ in range(int(input())):
    n,k,x = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    pref = [0]+list(accumulate(a))
    res = -inf
    def removeX(left,right,x):
        if right<0:
            return 0
        if right-x<0:
            return -pref[right+1]
        return -(pref[right+1]-pref[right-x+1]) + (pref[right-x+1] - pref[left])
    for i in range(k+1):
        left, right = 0, n-i-1
        res = max(removeX(left,right,x),res)
    print(res)
        
        