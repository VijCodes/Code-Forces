from itertools import permutations, combinations, product, accumulate, cycle, chain,groupby
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
from heapq import heapify,heappop,heappush,heappushpop,heapreplace
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
for _ in range(int(input())):
    n,k = map(int,input().split())
    s = input()
    l = list(map(int,input().split()))
    r = list(map(int,input().split()))
    q = int(input())
    x = list(map(int,input().split()))
    
