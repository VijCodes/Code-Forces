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
    s = input()
    pref = [0]+list(accumulate(list(map(int,list(s)))))
    period1 = [0]*n
    dp = [0]*n
    #print(pref)
    for i,val in enumerate(list(map(int,list(s)))):
        if i==0:
            if val==1:
                period1[i] = 0
            else:
                period1[i] = 1
        else:
            if i-k>=0:
                period1[i] = min(pref[i],period1[i-k]+(pref[i]-pref[i-k+1]))+int(val==0)
            else:
                period1[i] = pref[i]+int(val==0)
            dp[i] = min(period1[i],int(val==1)+dp[i-1],pref[i+1])
    print(dp[n-1])
    