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
    n = int(input())
    mapper = defaultdict(lambda:inf)
    for i in range(n):
        m,s = map(str,input().split())
        mapper[s] = min(mapper[s],int(m))
    res = min(mapper['11'],mapper['01']+mapper['10'])
    print(res if res!=inf else -1) 