from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
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
    n2,n3 = 0,0
    m2,m3 = 0,0
    nVal = n
    while nVal%2==0:
        nVal//=2
        n2+=1
    while nVal%3==0:
        nVal//=3
        n3+=1
    mVal = m
    while mVal%2==0:
        mVal//=2
        m2+=1
    while mVal%3==0:
        mVal//=3
        m3+=1
    if n3>=m3 and n2+n3>=m2+m3 and mVal==nVal and n2<=m2:
        print('YES')
    else:
        print('NO')
    