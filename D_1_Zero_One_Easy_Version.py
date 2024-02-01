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
    n,x,y = map(int,input().split())
    a = input()
    b = input()
    xor = [a[i]!=b[i] for i in range(n)]
    if sum(xor)%2:
        print(-1)
    else:
        if sum(xor)!=2:
            print(y*(sum(xor)//2))
        else:
            indexes = []
            for i,val in enumerate(xor):
                if val:
                    indexes.append(i)
            if indexes[0]!=indexes[1]-1:
                print(y)
            else:
                if indexes[0]>1 or n-indexes[1]-1>1:
                    print(min(x,2*y))
                else:
                    print(x)
            
        
    