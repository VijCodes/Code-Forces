from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb,ceil,floor
from sys import stdin,stdout
input = lambda: stdin.buffer.readline().decode().strip()
from heapq import heapify,heappop,heappush,heapreplace
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

for _ in range(int(input())):
    n,k = map(int,input().split())
    b = list(map(int,input().split()))
    factors = [7,17,17]
    counter = Counter(factors)
    res = True
    for val in b:
        if not counter[val] and val!=1 and val!=289 and val!=2023 and val!=17*7:
            res = False
            break
        elif val==2023:
            counter[17]-=2
            counter[7]-=1
            if counter[17]<0 or counter[7]<0:
                res = False
                break
        elif val==289:
            counter[17]-=2
            if counter[17]<0:
                res = False
                break
        elif val==17*7:
            counter[17]-=1
            counter[7]-=1
            if counter[17]<0 or counter[7]<0:
                res = False
                break
        else:
            counter[val]-=1
    add = 1
    add*=17**(counter[17])
    add*=7**(counter[7])
    ans = [add]+(k-1)*[1]
    if res:
        print('YES')
        print(*ans)
    else:
        print('NO')
        
    