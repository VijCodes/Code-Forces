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

def divisors(x):
    divisors = [1]
    for i in range(2,int(sqrt(x))+1):
        if x%i == 0:
            divisors.append(i)
            if i**2 != x:
                divisors.append(x//i)
    return divisors
#print(divisors(4))
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if n == 1:
        print(1)
        continue
    divs = divisors(n)
    #print(divs)
    res = 0
    for k in divs:
        gcd_num = a[k]-a[0]
        for i in range(k,n):
            gcd_num = gcd(gcd_num,a[i]-a[i-k])
        res += (gcd_num != 1)
    print(res+1)