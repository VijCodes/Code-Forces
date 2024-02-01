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

c = Counter()
for i in range(int(input())):
    t,v = map(int,input().split())
    if t==1:
        c[2**v]+=1
    else:
        for i in reversed(range(32)):
            k = min(c[2**i],v//(2**i))
            v-=k*(2**i)
            if not v:
                break
        if v:
            print('NO')
        else:
            print('YES')
    