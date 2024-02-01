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

@lru_cache
def calc(even,odd,index):
    if even+odd==1:
        return 0
    if index:
        if odd>=2:
            return calc(even+1,odd-2,abs(index-1))
        elif even>=2:
            return calc(even-1,odd,abs(index-1))
        else:
            return calc(even,odd-1,abs(index-1))-1
    else:
        if even and odd:
            return calc(even,odd-1,abs(index-1))-1
        elif even>=2:
            return calc(even-1,odd,abs(index-1))
        else:
            return calc(even+1,odd-2,abs(index-1))
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    res = []
    even,odd = 0,0
    summ = 0
    for val in a:
        summ+=val
        if val%2:
            odd+=1
        else:
            even+=1
        if even+odd==1:
            reduce = 0
        else:
            reduce = odd//3
            if odd%3==1:
                reduce+=1
        res.append(summ-reduce)
    print(*res)