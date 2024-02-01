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
    s = input()
    t = input()
    fixes = [0,0]
    for i in range(1,n):
        if s[i]==s[i-1]:
            if s[i]=='0':
                fixes[0]=1
            else:
                fixes[1]=1
    #print(fixes)
    canfix = [0,0]
    if t[0]==t[-1]:
        f = True
        for i in range(1,m):
            if t[i]==t[i-1]:
                f = False
                break
        if f and int(t[0]):
            canfix[0] = 1
        elif f:
            canfix[1] = 1
    #print(canfix)
    ans = True
    for i,val in enumerate(fixes):
        if fixes[i] and not canfix[i]:
            ans = False
    if ans:
        print('Yes')
    else:
        print('No')
            