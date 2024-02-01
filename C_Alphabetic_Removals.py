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

n,k = map(int,input().split())
s = input()
heap = []
heapify(heap)
lists = list(s)
for i,ch in enumerate(lists):
    heappush(heap,(ch,i))
remove = set()
for i in range(k):
    ch,index = heappop(heap)
    remove.add(index)
res = ''
for i,ch in enumerate(lists):
    if i not in remove:
        res+=ch
print(res)
        