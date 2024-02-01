from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
 
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
for _ in range(int(input())):
    n = int(input())
    a = input()
    consdot = 0
    curr = 0
    countDots = Counter(a)['.']
    for val in a:
        if val=='.':
            curr+=1
        else:
            curr = 0
        consdot = max(consdot,curr)
    if consdot>=3:
        print(2)
    else:
        print(countDots)
    