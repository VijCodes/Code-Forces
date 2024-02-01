from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
 
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

MOD = 998244353
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    carry = 1
    res = 0
    for val in a:
        carry = min(carry,val)
        res+=val-carry
        carry = max(val,carry)
    print(res)
    