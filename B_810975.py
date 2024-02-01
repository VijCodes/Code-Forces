from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
 
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

MOD = 998244353

# Precompute factorials and inverse factorials
f1 = [1] * (300001)
f2 = [1] * (300001)
for i in range(1, 300001):
    f1[i] = f1[i - 1] * i % MOD
f2[300000] = pow(f1[300000], MOD - 2, MOD)
for i in range(300000, 0, -1):
    f2[i - 1] = f2[i] * i % MOD

def C(n, m):
    if n < m: return 0
    if n < 0 or m < 0: return 0
    if n == m: return 1
    return f1[n] * f2[m] % MOD * f2[n - m] % MOD

def calc(n, m, k):
    res = 0
    ops = 1
    for i in range(m + 1):
        res = (res + ops * C(m, i) * C(m + k - 1 - i * n, m - 1) % MOD) % MOD
        ops *= -1
    return res

def solve(n, m, k):
    if m > n or k > m: return 0
    if m == 0: return 1
    if n == 0: return 1
    if k == 0: return 0
    return (calc(k + 1, n - m + 1, m) - calc(k, n - m + 1, m) + MOD) % MOD

n,m,k = map(int,input().split())
print(solve(n,m,k))