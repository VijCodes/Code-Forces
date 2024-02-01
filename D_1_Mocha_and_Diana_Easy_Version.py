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


n,m1,m2 = map(int,input().split())
par1 = [i for i in range(n+1)]
par2 = [j for j in range(n+1)]
ranks1 = [1 for i in range(n+1)]
ranks2 = [1 for j in range(n+1)]

def union1(node1,node2):
    r1,r2 = find1(node1),find1(node2)
    if r1==r2:return 
    rank1,rank2 = ranks1[r1],ranks1[r2]
    if rank1>rank2:
        ranks1[r1]+=ranks1[r2]
        par1[r2] = r1
    else:
        ranks1[r2]+=ranks1[r1]
        par1[r1] = r2
    return 

def find1(node):
    root = node
    while root!=par1[root]:
        root = par1[root]
    par1[node] = root
    return root

def union2(node1,node2):
    r1,r2 = find2(node1),find2(node2)
    if r1==r2:return 
    rank1,rank2 = ranks2[r1],ranks2[r2]
    if rank1>rank2:
        ranks2[r1]+=ranks2[r2]
        par2[r2] = r1
    else:
        ranks2[r2]+=ranks2[r1]
        par2[r1] = r2
    return 

def find2(node):
    root = node
    while root!=par2[root]:
        root = par2[root]
    par2[node] = root
    return root

for _ in range(m1):
    u,v = map(int,input().split())
    union1(u,v)
    
for _ in range(m2):
    u,v = map(int,input().split())
    union2(u,v)

res = []
for i in range(1,n+1):
    for j in range(1,n+1):
        if i!=j and find1(i)!=find1(j) and find2(i)!=find2(j):
            res.append((i,j))
            union1(i,j)
            union2(i,j)
print(len(res))
for l,m in res:
    print(str(l)+' '+str(m))

    

