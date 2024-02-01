from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain,groupby
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
#from copy import deepcopy
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    c = [0]*64
    MOD = 10**9+7
    #res = 0
    for val in a:
        #nc = deepcopy(c)
        for i in range(64):
            comb = i&val
            c[comb]=(c[i]+c[comb])%MOD
        c[val]+=1
    res = 0
    for i in range(64):
        if i.bit_count() == k:
            res+=c[i]
    print(res)  
        