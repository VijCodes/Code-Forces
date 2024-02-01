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

for i in range(int(input())):
    st = input()
    n = len(st)
    res = False
    for i in range(n-1):
        a = st[:i+1]
        b = st[i+1:]
        if a[0]!='0' and b[0]!='0' and int(b)>int(a) and int(b)>0 and int(a)>0:
            res = True
            a,b = int(a),int(b)
            break
    if res:
        print(f'{a} {b}')
    else:
        print(-1)
