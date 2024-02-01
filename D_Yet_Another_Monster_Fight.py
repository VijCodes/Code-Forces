from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
 
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

n = int(input())
a = list(map(int,input().split()))
carry1 = 0
carrf = [0]*n
carrb = [0]*n
for i,val in enumerate(a):
    carrf[i] = max(carry1,val-i)
    carry1 = carrf[i]
carry2 = 0
for i in reversed(range(n)):
    carrb[i] = max(carry2,a[i]-(n-i-1))
    carry2 = carrb[i] 
#print(carrf)
#print(carrb)
res = inf
for i in range(n):
    curr = a[i]
    if i<n-1:
        curr = max(curr,carrb[i+1]+n-1)
    if i>0:
        curr = max(curr,carrf[i-1]+n-1)
    res = min(res,curr)
print(res)

