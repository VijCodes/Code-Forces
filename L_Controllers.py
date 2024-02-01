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

n = int(input())
s = input()
p = Counter(s)['+']
m = n-p
q = int(input())
for _ in range(q):
    a,b = map(int,input().split())
    if a==b:
        if p==m:
            print('YES')
        else:
            print('NO')
    else:
        rem = ((p-m)*a)%(a-b)
        div = ((p-m)*a)//(a-b)
        #print(div,m,p)
        if rem or div<-m or div>p:
            print('NO')
        else:
            print('YES')