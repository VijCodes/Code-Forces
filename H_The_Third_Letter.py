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
def bfs(i):
    search = [i]
    seen.add(i)
    while search:
        node = search.pop()
        for dis,ch in order[node]:
            if ch in seen:
                if res[ch]!=res[node]+dis:
                    return False
            else:
                search.append(ch)
                seen.add(ch)
                res[ch] = res[node]+dis
    return True

for j in range(int(input())):
    n,m = map(int,input().split())
    order = defaultdict(list)
    res = [0]*n
    for _ in range(m):
        a,b,d = map(int,input().split())
        order[b-1].append([d,a-1])
        order[a-1].append([-d,b-1])
    seen = set()
    ans = True
    for i in range(n):
        if i not in seen and not bfs(i):
            ans = False
            break
    if ans:
        print('YES')
    else:
        print('NO')
            