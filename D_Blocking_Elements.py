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
    pref_sum = [0] + list(accumulate(a))
    
    def check(val):
        n = len(a)
        dp = [inf]* (n + 1) # minimum sum 
        dp[0] = 0
        stack = deque([0])
        for i in range(n):    
            while stack and pref_sum[i] - pref_sum[stack[0]] > val:
                stack.popleft()
            if stack:
                dp[i + 1] = dp[stack[0]] + a[i]
            else:
                dp[i + 1] = a[i]
            while stack and dp[stack[-1]]>=dp[i + 1]:
                stack.pop()
            stack.append(i + 1)
        res = inf
        sum = 0
        for i in reversed(range(n)):
            if sum>val:
                break
            res = min(dp[i + 1], res)
            sum += a[i]
        return res<=val
    
    left = max(a)-1
    right = sum(a)
    while left <= right:
        mid = left + (right - left)//2
        if check(mid):
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    print(res)
    
    