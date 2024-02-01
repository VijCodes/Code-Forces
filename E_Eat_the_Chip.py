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
    h,w,xa,ya,xb,yb = map(int,input().split())
    xa,ya = ya,xa
    xb,yb = yb,xb
    if yb<=ya:
        print('Draw')
        continue
    
    def win_loss(x1,y1,x2,y2,alice = True):
        steps = abs((y1-y2))
        if x1!=x2:
            gap = abs(x2-x1)
            avoid = w-x2 if x2>x1 else x2-1
            if alice:
                gap-=1
                steps-=1  
            avoid = min(avoid,steps//2)
            return steps//2>=gap+avoid
        else:
            return True
            
    if (ya-yb)%2: ## alice playing for win
        print('Alice' if win_loss(xa,ya,xb,yb) else 'Draw')
    else: ## bob playing for win
        print('Bob' if win_loss(xb,yb,xa,ya,False) else 'Draw')