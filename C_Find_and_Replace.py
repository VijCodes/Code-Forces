from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb
from sys import stdin
input = lambda: stdin.buffer.readline().decode().strip()
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
for _ in range(int(input())):
    n = int(input())
    s = input()
    c = defaultdict(set)
    for i,ch in enumerate(list(s)):
        c[ch].add(i%2)
    res = True
    for ch,st in c.items():
        if len(st)==2:
            res = False
            break
    if res:
        print('YES')
    else:
        print('NO')