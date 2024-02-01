from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

for _ in range(int(input())):
    n = int(input())
    s = input()
    adj = defaultdict(lambda:[0,0])
    for i in range(n):
        l,r = map(int,input().split())
        adj[i+1] = [l,r]
    res = inf
    search = deque([(1,0)])
    seen = {1}
    while search:
        node,changes = search.popleft()
        if adj[node][0] ==0 and adj[node][1]==0:
            res = min(res,changes)
        if adj[node][0] and adj[node][0] not in seen:
            newchange = changes+int(s[node-1]!='L')
            search.append((adj[node][0],newchange))
            seen.add(adj[node][0])
        if adj[node][1] and adj[node][1] not in seen:
            newchange = changes+int(s[node-1]!='R')
            search.append((adj[node][1],newchange))
            seen.add(adj[node][1])
    print(res)
        