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
def nextBounce(point,direction): 
    x,y = direction
    if direction[0] == 1:
        xwd = n-1-point[0]
    else:
        xwd = point[0]
    if direction[1] == 1:
        ywd = m-1-point[1]
    else:
        ywd = point[1]
    if xwd>ywd:
        nx,ny = (x-ywd)%n,0
        ndirection = (-1,1) 
    elif xwd ==ywd:
        nx,ny = (n-1,m-1)
        ndirection = (-direction[0],-direction[1])
    else: 
        nx,ny = 0,(y-xwd)%m
        ndirection = (1,-1)
    new_x,new_y = side[0]*x,side[1]*y
for _ in range(int(input())):
    n,m,i1,j1,i2,j2,d = map(int,input().split())
    corners = {(0,0),(0,m-1),(n-1,0),(n-1,m-1)}
    