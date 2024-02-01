from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb,ceil,floor
from sys import stdin,stdout
input = lambda: stdin.buffer.readline().decode().strip()
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

n,k = map(int,input().split())
a = list(map(int,input().split()))
pref = list(accumulate(a,initial = 0)) # prei represents summ before the index i
res = 0
for i in range(k-1,n):
    for j in range(i-k+2):
        average = (pref[i+1]-pref[j])/(i-j+1)
        res = max(average,res)
print(res)
        