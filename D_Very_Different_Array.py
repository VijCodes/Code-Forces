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
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a = deque(sorted(a))
    b = deque(sorted(b))
    res = 0
    #print(a)
    #print(b)
    while a:
        maxi = max(abs(a[0]-b[0]),abs(a[0]-b[-1]),abs(a[-1]-b[-1]),abs(a[-1]-b[0]))
        if abs(a[0]-b[0])>=maxi:
            res += abs(a.popleft()-b.popleft())
            #print('if - 1')
        elif abs(a[0]-b[-1])>=maxi:
            res += abs(a.popleft()-b.pop())
            #print('if - 2')
        elif abs(a[-1]-b[-1])>=maxi:
            res += abs(a.pop()-b.pop())
            #print('if - 3')
        else:
            res += abs(a.pop()-b.popleft())
            #print('if - 4')
        #print(res)
    print(res)