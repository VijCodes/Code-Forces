from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain,groupby
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
n = int(input())
a = list(map(int,input().split()))
s = set(a)
b = sorted(list(s),reverse = True)
def invert(n):
    l = n.bit_length()
    return n^((1<<l) - 1)

maxB = b[0].bit_length()
f = [-1]*2**maxB
for val in reversed(range(2**maxB)):
    comp = invert(val)
    f[comp] = comp if comp in s else -1
    for i in range(maxB):
        if f[comp]!=-1:
            break
        if comp&(1<<i):
            f[comp]=f[comp^(1<<i)]
res = [-1]*len(a)
for i,v in enumerate(a):
    res[i] = f[invert(v)]
print(res)

        