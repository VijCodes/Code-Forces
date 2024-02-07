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

n, m = map(int,input().split())
a = list(map(int,input().split()))
sum_awesome = n*(n+1)//2 
for i in range(n):
    if i and a[i] != a[i-1]:
        sum_awesome += i*(n-i)
for _ in range(m):
    i, x = map(int,input().split())
    i -= 1
    if i and a[i] != a[i-1]:
        sum_awesome -= i*(n-i)
    if i + 1 < n and a[i + 1] != a[i]:
        sum_awesome -= (i + 1)*(n-i-1)
    if i and x != a[i-1]:
        sum_awesome += i*(n-i)
    if i + 1 < n and a[i + 1] != x:
        sum_awesome += (i + 1)*(n-i-1)
    a[i] = x
    print(sum_awesome)
