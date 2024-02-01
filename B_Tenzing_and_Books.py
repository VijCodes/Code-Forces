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
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    ai,bi,ci = True,True,True
    num = 0
    res = False
    for i in range(n):
        if (~x)&(a[i]):
            ai = False
        if (~x)&(b[i]):
            bi = False
        if (~x)&(c[i]):
            ci = False
        if ai:
            num|=a[i]
        if bi:
            num|=b[i]
        if ci:
            num|=c[i]
        if num==x:
            res = True 
            break               
    print('YES' if res else 'NO')