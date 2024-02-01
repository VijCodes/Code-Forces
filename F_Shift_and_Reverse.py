from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb

#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

for _ in range(int(input())):
    n = int(input())
    ar = list(map(int,input().split())) 
    arR = ar[::-1]
    res = inf
    def findShifts(a):
        i = 1
        while i<n:
            if a[i]<a[i-1]:
                break
            i+=1
        if i==n:
            res = 0
        else:
            s,shifts = i+1,n-i
            res = inf
            while s<n:
                if a[s]<a[s-1]:
                    break
                s+=1
            if s==n and a[-1]<=a[0]:
                res = shifts
        return res
    op1 = findShifts(ar)
    op2 = findShifts(arR) 
    res = min(min(op1,abs(n-op1)+2),min(op2,abs(n-op2))+1)
    print(res if res!=inf else -1)
    