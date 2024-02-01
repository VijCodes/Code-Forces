from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
 
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
def prime_factors(n):
    while n % 2 == 0:
        c[2]+=1
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            c[i]+=1
            n //= i
        i += 2
    if n > 2:
        c[n]+=1
    return
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    c = Counter()
    for val in arr:
        prime_factors(val)
    ans = 'YES'
    for val,cnt in c.items():
        if cnt%n:
            ans = 'NO'
            break
    print(ans)