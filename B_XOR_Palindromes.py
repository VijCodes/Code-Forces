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
    s = input()
    diff = 0
    for i in range(len(s)//2):
        if s[i]!=s[n-i-1]:
            diff+=1
    res = ''
    for x in range(n+1):
        if n%2:
            ans = str(int(min(x,n-x)>=diff))
            res+= '1' if min(x,n-x)>=diff else '0'
        else:
            res+= '1' if min(x,n-x)>=diff and x%2==diff%2 else '0'
    print(res)
    
    
  