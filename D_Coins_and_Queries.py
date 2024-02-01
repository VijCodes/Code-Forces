from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb,ceil,floor
from copy import deepcopy
from sys import stdin,stdout
input = lambda: stdin.buffer.readline().decode().strip()
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

n,q = map(int,input().split())
a = list(map(int,input().split()))
c = Counter(a)
for _ in range(q):
    b = int(input())
    #nc = deepcopy(c)
    res = 0
    for i in reversed(range(32)):
        k = min(c[2**i],b//(2**i))
        res+=k
        b-=k*(2**i)
        if not b:
            break
    if b:
        print(-1)
    else:
        print(res)        