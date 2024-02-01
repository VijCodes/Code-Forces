from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb
from sys import stdin,stdout
input = lambda: stdin.buffer.readline().decode().strip()
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
def check(l,r):
    ans = ['?']+[r-l+1]+list(range(l+1,r+2))
    print(' '.join(list(map(str,ans))))
    stdout.flush()
    x = int(input())
    if x>pre[r+1]-pre[l]:
        return True
    else:
        return False
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    pre = [0]+list(accumulate(a)) # pre_i represents summ before the index i
    l,r = 0,n-1
    while r>=l:
        mid = l+(r-l)//2
        if check(l,mid):
            r = mid-1
            res = mid
        else:
            l = mid+1
    print(f'! {res+1}')
    stdout.flush()
        
    