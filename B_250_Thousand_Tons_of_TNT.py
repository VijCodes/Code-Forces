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
    n = int(input())
    a = list(map(int,input().split()))
    pref = [0]+list(accumulate(a))
    divisors = [1]
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            divisors.append(i)
            if n//i!=i:
                divisors.append(n//i)
    res = 0
    for div in divisors:
        maxi,mini = -inf,inf
        for i in range(div,n+1,div):
            maxi = max(pref[i]-pref[i-div],maxi)
            mini = min(pref[i]-pref[i-div],mini)
        res = max(res,maxi-mini)
    print(res)