from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb
from sys import stdin,stdout
input = lambda: stdin.buffer.readline().decode().strip()

for _ in range(int(input())):
    n = int(input())
    c = list(map(int,input().split()))
    summ = 1
    c.sort()
    res = True
    if c[0]!=1:
        res = False
    for val in c[1:]:
        if summ<val:
            res = False
            break
        else:
            summ+=val
    if res:
        print('YES')
    else:
        print('NO')