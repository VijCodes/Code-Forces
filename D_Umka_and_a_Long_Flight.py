from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split())))
# int(input())
F = [1]*46
for i in range(2,46):
    F[i]=F[i-2]+F[i-1]
def helper(n,x,y):
    if n<=1:
        return True
    if y-F[n]>0:
        x,y = y-F[n],x
        return helper(n-1,x,y)
    elif y+F[n]<=F[n+1]:
        x,y = y,x
        return helper(n-1,x,y) 
    else:
        return False
    
for _ in range(int(input())):
    n,x,y =map(int,input().split())
    if helper(n,x,y):
        print('YES')
    else:
        print('NO')