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

n,m = map(int,input().split())
a = list(map(int,input().split()))
counter = Counter()
for val in a:
    counter[val%m]+=1
surplus = []
res = 0
shifts = defaultdict(list)
for rem in range(2*m):
    rem = rem%m
    curr_surr = counter[rem]-n//m
    if curr_surr>0:
        surplus+=[rem]*curr_surr
    else:
        i = 0
        while surplus and i<-curr_surr:
            item = surplus.pop()
            res+=(rem-item)%m
            shifts[item].append(rem)
            counter[item]-=1
            counter[rem]+=1
            i+=1
for i in range(n):
    rem = a[i]%m
    if shifts[rem]:
        shift_to = shifts[rem].pop()
        a[i]+=(shift_to-rem)%m
print(res)
print(*a)