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
    s = input()
    Acnt = 0
    Bcnt = 0
    for ch in s[::-1]:
        if ch=='A':
            if Bcnt:
                Bcnt-=1
            else:
                Acnt+=1
        else:
            Bcnt+=1
    print(Acnt+(Bcnt%2))