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
    neg,highIndex = False,-1
    maxi = -inf
    for i,val in enumerate(a):
        if abs(val)>maxi:
            if val<=0:
                neg = True
            else:
                neg = False
            maxi = abs(val)
            highIndex = i+1 # 1 index
    if neg:
        print(2*n)
        for i in reversed(range(n)):
            if i==n-1:
                print(i+1,highIndex)
                print(i+1,highIndex)
            else:
                print(i+1,i+2)
                print(i+1,i+2)
    else:
        print(2*n)
        for i in range(n):
            if i==0:
                print(i+1,highIndex)
                print(i+1,highIndex)
            else:
                print(i+1,i)
                print(i+1,i)  