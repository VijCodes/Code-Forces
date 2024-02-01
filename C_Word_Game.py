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
    a = list(map(str,input().split()))
    b = list(map(str,input().split()))
    c = list(map(str,input().split()))
    res = [0,0,0]
    wordL = defaultdict(list)
    for i in range(n):
        wordL[a[i]].append(0)
        wordL[b[i]].append(1)
        wordL[c[i]].append(2)
    for w,lst in wordL.items():
        if len(lst)==1:
            res[lst[0]]+=3
        elif len(lst)==2:
            for l in lst:
                res[l]+=1
    print(' '.join(map(str,res)))