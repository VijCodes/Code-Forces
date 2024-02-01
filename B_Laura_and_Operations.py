from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    res = [0, 0, 0]
    if abs(a-b)%2==0:
        c>=abs(a-b)//2
        res[2]=1
    if abs(c-b)%2==0:
        a>=abs(c-b)//2
        res[0]=1
    if abs(a-c)%2==0:
        b>=abs(a-c)//2
        res[1]=1
    print(' '.join(map(str,res)))

    