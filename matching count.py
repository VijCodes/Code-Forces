#https://atcoder.jp/contests/dp/tasks/dp_o?lang=en
from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
#from sortedcontainers import SortedList
from heapq import heappush,heapify,heappushpop,heappop,_heapify_max,heapreplace

mat = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

n = len(mat)
arr = list(range(n))
MOD = 10**9+7
dp = [0]*(1<<n)
dp[0] = 1

for j in range(1<<n):
    i = j.bit_count()-1
    for k in range(n):
        if (1<<k)&j and mat[i][k] == 1:
                dp[j]=(dp[j]+dp[(1<<k)^j])%MOD
print(dp[(1<<n)-1])


