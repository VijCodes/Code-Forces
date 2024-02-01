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

for j in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if 0 in a:
        print(0)
    else:
        negs = sum([val<0 for val in a])
        if negs%2:
            print(0)
        else:
            print(1)
            print(str(1)+' '+'0')