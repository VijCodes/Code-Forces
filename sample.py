# **** Packages **** #
from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd

##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

MOD = 998244353
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
m = int(input())
c = list(map(int,input().split()))
d = list(map(int,input().split()))

xMap = defaultdict(int)
for i in range(n):
    xMap[a[i]] = b[i]

yMap = defaultdict(int)
for i in range(m):
    yMap[c[i]] = d[i]

res = 1

for i in range(n):
    if xMap[a[i]]>yMap[a[i]]:
        res = res*2%MOD
    elif xMap[a[i]]<yMap[a[i]]:
        res = 0
        break
    
for j in range(m):
    if xMap[c[j]]<yMap[c[j]]:
        res = 0
    
print(res)