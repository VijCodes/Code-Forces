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
    n = int(input())
    par = list(map(int,input().split()))
    s = input()
    adj = defaultdict(list)
    for i,val in enumerate(par):
        adj[val].append(i+2)
    stack1 = [1]
    stack2 = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        for ch in adj[node]:
            stack1.append(ch)
    color_count = defaultdict(lambda:[0,0])
    res = 0
    while stack2:
        node = stack2.pop()
        chg_i = 0 if s[node-1]=='B' else 1
        color_count[node][chg_i]+=1
        color_count[par[node-2]][0] += color_count[node][0]
        color_count[par[node-2]][1] += color_count[node][1] 
        res+=color_count[node][0]==color_count[node][1]
    print(res)