from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain,groupby
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
for _ in range(int(input())):
    n,m = map(int,input().split()) # length,number of segments
    seg = []
    for _ in range(m):
        l,r = map(int,input().split()) #segment boundaries
        seg.append([l,r])
    q = int(input()) # number of changes
    ch = []
    for _ in range(q):
        ch.append(int(input()))
    def check(i):
        a = [0]*n
        for x in ch[:i]:
            a[x-1]=1
        prefS = [0]+list(accumulate(a))
        for l,r in seg:
            if prefS[r]-prefS[l-1]>(r-l+1)//2:
                return True
        return False
    if not check(q):
        print(-1)
        continue
    left = 1
    right = q
    while left<=right:
        mid = left+(right-left)//2
        if check(mid):
            res = mid
            right = mid-1
        else:
            left = mid+1
    print(res)