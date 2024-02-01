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

for i in range(int(input())):
    s = input()
    c = Counter(s)
    res = len(s)
    for ch in s:
        need = str(abs(int(ch)-1))
        if c[need]:
            c[need]-=1
            res-=1
        else:
            break
    print(res)