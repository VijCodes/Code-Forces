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
    m = int(input())
    pref_right = [0]*(n+1)
    pref_left = [0]*(n+1)
    for i in range(n):
        if i == 0:
            pref_left[i] = 0
        elif i == 1:
            pref_left[i] = 1
        else:
            if (a[i]-a[i-1]) < (a[i-1]-a[i-2]):
                pref_left[i] = pref_left[i-1] + 1
            else:
                pref_left[i] = pref_left[i-1] + (a[i]-a[i-1])
    
    for i in reversed(range(n)):
        if i == n-1:
            pref_right[i] = 0
        elif i == n-2:
            pref_right[i] = 1
        else:
            if (a[i+1]-a[i]) < (a[i+2]-a[i+1]):
                pref_right[i] = pref_right[i+1] + 1
            else:
                pref_right[i] = pref_right[i+1] + (a[i+1]-a[i])
    
    #print(pref_left)
    #print(pref_right)
    for _ in range(m):
        x, y = map(int,input().split())
        if x<y:
            print(pref_left[y-1]-pref_left[x-1])
        else:
            print(pref_right[y-1]-pref_right[x-1])
    