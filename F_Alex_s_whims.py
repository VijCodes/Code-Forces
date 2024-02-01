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
    n,q = map(int,input().split())
    for i in range(n-2):
        print(str(i+2)+' '+str(i+3))
    print('1 3')
    pastD = 2
    for _ in range(q):
        d = int(input())
        if pastD ==d:
            res = [-1,-1,-1]
        else:
            res = [1,pastD+1,d+1]
        pastD = d
        print(' '.join(map(str,res)))
    
    