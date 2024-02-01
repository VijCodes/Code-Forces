from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb,ceil,floor
from sys import stdin,stdout
input = lambda: stdin.buffer.readline().decode().strip()
from heapq import heapify,heappop,heappush,heapreplace
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

for _ in range(int(input())):
    n = int(input())
    s = input()
    accu = ''
    def poss(accu):
        if 'B' not in accu or 'R' not in accu:
            return False
        return True
    res = True
    for ch in s:
        if ch=='W' and accu:
            if not poss(accu):
                res = False
                break
            accu = ''
        elif ch!='W':
            accu+=ch
    if accu and not poss(accu):
        res = False
    print('YES') if res else print('NO')
        