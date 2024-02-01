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
 
def main():
	n,m=map(int,input().split())
	gf=defaultdict(list)
	gb=defaultdict(list)
	for _ in range(m):
		u,v,w=map(int,input().split())
		gf[u].append((v,w))
		gb[v].append((u,w))
	dis=[float('inf')]*(n+1)
	dis[1]=0
	h=[]
	heapify(h)
	heappush(h,(0,1))
	while h:
		cd,cn=heappop(h)
		if dis[cn]==cd:
			for nn,nw in gf[cn]:
				if cd+nw<dis[nn]:
					dis[nn]=cd+nw
					heappush(h,(nw+cd,nn))
	res=[float('inf')]*(n+1)
	res[1]=0
	h=[]
	for i in range(1,n+1):
		if dis[i]!=float('inf'):
			res[i]=dis[i]
			h.append((dis[i],i))
	heapify(h)
	while h:
		cd,cn=heappop(h)
		if res[cn]==cd:
			for nn,nw in gb[cn]:
				if cd+nw<res[nn]:
					res[nn]=cd+nw
					heappush(h,(nw+cd,nn))
	for i in range(1,len(res)):
		if res[i]==float('inf'):res[i]=-1
	print(*res[2:])
 
main()
    
    