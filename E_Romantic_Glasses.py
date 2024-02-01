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
    aEven = [val if i%2==0 else 0 for i,val in enumerate(a)]
    aOdd = [val if i%2 else 0 for i,val in enumerate(a)]
    prefEven = [0]+list(accumulate(aEven))
    prefOdd = [0]+list(accumulate(aOdd))
    seen = set()
    res = False
    for i in range(n+1):
        diff = prefEven[i]-prefOdd[i]
        if diff in seen:
            res = True
            break
        else:
            seen.add(diff)
    print('YES' if res else 'NO')