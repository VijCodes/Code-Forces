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
def isBipartite(graph,n) -> bool:
    color = ['B']*n # R is red, B is black
    search = list(range(n))
    seen = set()
    while search:
        node = search.pop()
        if node in seen:
            continue
        else:
            seen.add(node)
        col = color[node]
        for ch in graph[node]:
            if ch in seen:
                if color[ch]==col:
                    return False
            else:
                #seen.add(ch)
                color[ch] = 'B' if col == 'R' else 'R'
                search.append(ch)
    return True
def solve():
    n = int(input())
    adj = defaultdict(list) # store counter indexes
    res = True
    numToInd = defaultdict(list) # store indices for a number
    for i in range(n):
        a,b = map(int,input().split())
        if res:
            if a==b:
                res = False
            for opp in numToInd[a]:
                adj[opp].append(i)
                adj[i].append(opp)
            for opp in numToInd[b]:
                adj[opp].append(i)
                adj[i].append(opp)
            numToInd[a].append(i)
            numToInd[b].append(i)
            if len(numToInd[a])>2 or len(numToInd[a])>2:
                res = False
    # does adjacency matrix represent a bipartite graph
    if res:
        res = isBipartite(adj,n)
    if res:
        print('YES')
    else:
        print('NO')
for _ in range(int(input())):
    solve()