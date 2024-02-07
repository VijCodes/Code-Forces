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


n, q = map(int,input().split())
bits = [['x' for j in range(30)] for i in range(n)]
que = []
one_adj = defaultdict(list)
for _ in range(q):
    i, j, x = map(int,input().split())
    i -= 1
    j -= 1
    
    if i == j:
        for ind in range(30):
            bits[i][ind] = int((1<<ind)&x > 0)
        continue
    
    que.append([i, j, x])
    for ind in range(30):
        if (1<<ind)&x:
            one_adj[i].append(j)
            one_adj[j].append(i)
        else:
            bits[i][ind] = 0
            bits[j][ind] = 0
            
for i, j, x in que:
    for ind in range(30):
        if (1<<ind)&x:
            if bits[i][ind] == 0:
                bits[j][ind] = 1
            elif bits[j][ind] == 0:
                bits[i][ind] = 1
                
que = sorted(que, key = lambda x: min(x[0], x[1]))

for i, j, x in que:
    for ind in range(30):
        if (1<<ind)&x:
            if bits[i][ind] == 'x' and bits[j][ind] == 'x':
                bits[min(i, j)][ind] = 0
                bits[max(i, j)][ind] = 1
                for ch in one_adj[min(i,j)]:
                    bits[ch][ind] = 1

res = [0]*n
for i in range(n):
    for j in range(30):
        if bits[i][j] == 1:
            res[i] += (1<<j)

print(*res)
                
                                