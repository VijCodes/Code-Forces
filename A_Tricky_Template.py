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
    strings = []
    for i in range(3):
        strings.append(input())
    res = False
    for i in range(n):
        if strings[0][i] !=  strings[1][i] and strings[1][i] != strings[2][i] and strings[0][i] != strings[2][i]:
            res = True
        elif strings[0][i] == strings[1][i] and strings[1][i] != strings[2][i]:
            res = True
    print('YES' if res else 'NO')