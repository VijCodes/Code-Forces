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
    n, q = map(int,input().split())
    a = list(map(int,input().split()))
    sorted_lst = []
    summ = 0
    for i, val in enumerate(a):
        summ += val
        if val == 1:
            sorted_lst.append(i)
    for _ in range(q):
        query = list(map(int,input().split()))
        if len(query) == 2:
            s = query[1]
            if not sorted_lst:
                if s <= summ and s%2 == 0:
                    print('YES')
                else:
                    print('NO')
            else:
                min2 = min(sorted_lst[0], n - sorted_lst[-1] - 1)
                if s > summ:
                    print('NO')
                elif summ%2 == s%2:
                    print('YES')
                elif s <= summ - 2*min2:
                    print('YES')
                else:
                    print('NO') 
        if len(query) == 3:
            i, v = query[1:]
            if a[i] == 1:
                sorted_lst.remove(i)
            if v == 1:
                sorted_lst.add(i)
            summ += - a[i] + v
            