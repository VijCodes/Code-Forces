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
    n,c = map(int,input().split())
    s = list(map(int,input().split()))
    ss = sum([val**2 for val in s])
    summ = sum(s)
    a,b,c = 4*n,4*summ,ss-c
    #print(a,b,c)
    print(int((sqrt(b**2-4*a*c)-b)/(2*a)))