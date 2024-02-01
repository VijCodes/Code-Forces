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
    n, k, m = map(int,input().split())
    check_sets = [set([chr(ordinal + ord('a')) for ordinal in range(k)]) for i in range(n)]
    s = input() 
    res = True
    last_removed = ''
    for ch in s:
        if len(check_sets[-1]) == 0:
            check_sets.pop()
        if len(check_sets) == 0:
            break
        if ch in check_sets[-1]:
            if len(check_sets[-1]) == 1:
                last_removed += ch
            check_sets[-1].remove(ch)    
    if check_sets and len(check_sets[-1]) == 0:
            check_sets.pop()
            
    res = (len(check_sets) == 0)
    if res:
        print('YES')
    else:
        print('NO')
        res_ch = list(check_sets[-1])[0]
        print(last_removed + res_ch*len(check_sets))
        