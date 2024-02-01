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

n,k = map(int,input().split())
a = list(map(int,input().split()))
if len(set(a))<k:
    print('NO')
else:
    team = list(set(a))
    valtoI = defaultdict(int)
    res = []
    for i,val in enumerate(a):
        valtoI[val] = i+1
    for i in range(k):
        res.append(valtoI[team[i]])
    print('YES')
    print(' '.join(map(str,res)))        