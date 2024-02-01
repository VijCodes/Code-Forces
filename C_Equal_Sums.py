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

k = int(input())
a = []
n = []
c = Counter()
res = False
for row in range(k):
    n.append(int(input()))
    l = list(map(int,input().split()))
    summ = sum(l)
    for col,val in enumerate(l):
        if summ-val in c:
            ans = []
            ans.extend(c[summ-val])
            ans.extend([row+1,col+1])
            res = True
            break
    if res:
        break
    for col,val in enumerate(l):
        c[summ-val] = [row+1,col+1]
if res:
    print('YES')
    print(f'{ans[0]} {ans[1]}')
    print(f'{ans[2]} {ans[3]}') 
else:
    print('NO')   