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
    n,q = map(int,input().split())
    a = list(map(int,input().split())) # n integers
    x = list(map(int,input().split())) # q integers 1<=x<=30
    DivSets = [set() for i in range(30)] 
    for i,val in enumerate(a):
        curr = val
        total = 0
        while curr and curr%2==0:
            total+=1
            curr//=2
        DivSets[total].add(i)
    for q in x:
        for div in range(q,30):
            rem = set()
            for ind in DivSets[div]:
                a[ind]+=(1<<(q-1))
                rem.add(ind)
            DivSets[div]-=rem
            DivSets[q-1]|=rem
    print(*a)