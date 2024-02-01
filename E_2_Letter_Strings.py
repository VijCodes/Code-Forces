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
    c = defaultdict(int)
    res = 0
    for _ in range(n):
        s = input()
        for od in range(ord('a'),ord('k')+1):
            if chr(od)!=s[0]:
                res+=c[chr(od)+s[1]]
        for od in range(ord('a'),ord('k')+1):
            if chr(od)!=s[1]:
                res+=c[s[0]+chr(od)]
        c[s]+=1
    print(res)
                        
    