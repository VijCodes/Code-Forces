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
    res = [0]*n
    heap = [(-n,0,n-1)] # add segment boundaries
    heapify(heap)
    curr = 1
    while heap:
        length,left,right = heappop(heap)
        if left==right:
            res[left]=curr
        else:
            index = left+(right-left)//2
            res[index]=curr
            if index-left:
                heappush(heap,(-(index-left),left,index-1))
            if right-index:
                heappush(heap,(-(right-index),index+1,right))
        #print(heap)
        curr+=1
    
    print(' '.join(map(str,res)))
        