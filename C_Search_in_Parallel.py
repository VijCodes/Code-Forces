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
    n,s1,s2 = map(int,input().split())
    r = list(map(int,input().split()))
    a = []
    b = []
    slotA,slotB = s1,s2
    r = sorted([(r[i],i+1) for i in range(n)])
    #print(r)
    while r:
        times,index = r.pop()
        if slotA>=slotB:
            b.append(index)
            slotB+=s2
        else:
            a.append(index)
            slotA+=s1
    print(str(len(a))+' '+' '.join(map(str,a)))
    print(str(len(b))+' '+' '.join(map(str,b)))