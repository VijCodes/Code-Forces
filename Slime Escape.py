from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
 
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    l,r = k-2,k
    health = a[k-1]
    deltaR,maxR = 0,0
    deltaL,maxL = 0,0
    ind = True
    while l>=0 and r<n and ind:
        ind = False
        while r<n and a[r]+deltaR+health+maxL>=0:
            ind = True
            deltaR+=a[r]
            maxR = max(deltaR,maxR)
            r+=1
        while l>=0 and a[l]+maxR+deltaL+health>=0:
            ind = True
            deltaL+=a[l]
            maxL = max(deltaL,maxL)
            l-=1
    if ind:
        print('Yes')
    else:
        print('No')