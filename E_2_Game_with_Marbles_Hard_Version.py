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
    b = list(map(int,input().split()))
    score = 0
    heap = [[a[i],b[i]] for i in range(n)]
    heap = sorted(heap,key = lambda x:abs(x[0]+x[1]))
    turn = 1
    while heap:
        if turn:
            aSc,bSc = heap.pop()
            score+=aSc-1
        else:
            aSc,bSc = heap.pop()
            score-=bSc-1
        turn = abs(turn-1)
    print(score)

    