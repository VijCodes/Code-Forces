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
    n,m = map(int,input().split())
    a = [1]+list(map(int,input().split()))
    b = list(map(int,input().split()))
    da = deque(sorted(a))
    db = deque(sorted(b))
    res = 0
    i = 0
    while db:
        if db[i]>da[i]:
            da.popleft()
            db.popleft()
        else:
            da.pop()
            db.popleft()
            res+=1
    print(res)
        