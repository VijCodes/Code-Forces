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
    a = list(map(int,input().split()))
    even = sum([val for val in a if val%2==0])
    odd = sum(a)-even
    if odd>=even:
        print('NO')
    else:
        print('YES')