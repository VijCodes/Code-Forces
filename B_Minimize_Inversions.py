from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect, bisect_left, bisect_right, insort
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
    b = list(map(int,input().split()))
    combined = sorted(list(zip(a, b)), key = lambda x:(x[0] + x[1]))
    small_a = []
    small_b = []
    res = 0
    for ai, bi in combined:
        small_a.append(ai)
        small_b.append(bi)
    print(*small_a)
    print(*small_b)