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
    n,m = map(int,input().split())
    c = Counter()
    for _ in range(m):
        u,v = map(int,input().split())
        c[u]+=1
        c[v]+=1
    single = 0
    for val,cnt in c.items():
        if cnt==1:
            single+=1
    x = n-single-1
    y = single//x
    print(str(x)+' '+str(y))