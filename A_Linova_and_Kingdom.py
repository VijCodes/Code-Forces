from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb

#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
n,k = map(int,input().split())
adj = defaultdict(list)
for i in range(n-1):
    u,v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
res = 0 
t = n-k
search = deque([(1,-1,-1)])
while search:
    node,score,par = search.popleft()
    if not t:
        res+=score
    for ch in adj[node]:
        if ch!=par:
            if t:
                search.append(ch,score+1,node)
                t-=1
            else:
                search.append(ch,score,node)
                
    