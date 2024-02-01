from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb,ceil,floor
from sys import stdin,stdout
input = lambda: stdin.buffer.readline().decode().strip()

#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
MOD = 998244353
for i in range(int(input())):
    n,x,y = map(int,input().split())
    diff = y-x
    for i in range(1,diff+1):
        if diff%i==0 and n>(diff//i):
            diff = i
            break
    res = []
    nex = y
    while n and nex>0:
        res.append(nex)
        n-=1
        nex-=diff
    nex = y+diff
    while n:
        res.append(nex)
        nex+=diff
        n-=1
    print(' '.join(map(str,res)))