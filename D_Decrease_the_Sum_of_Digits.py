from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb,ceil,floor
from sys import stdin,stdout
input = lambda: stdin.buffer.readline().decode().strip()

#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
MOD = 998244353
for i in range(int(input())):
    n,s = map(str,input().split())
    def modify(n,s):
        currS = 0
        add = ''
        index = -1
        for i,ch in enumerate(list(n)):
            currS+=int(ch)
            if currS>s:
                last = int(ch)
                index = i
        if index==-1:
            return n
        index-=1
        if last!=1:
            while True:
                if int(n[index])!=9:
                    new = list(n)
                    new[index] = str(int(n[index]-1))
                    for i in range(index+1,len(new)):
                        new[index]=str(0)
                    new = ''.join(new)
                    return modify(new,s)
                index-=1
        else:
            while True:
                if int(n[index])!=0:
                    new = list(n)
                    new[index] = str(int(n[index]-1))
                    for i in range(index+1,len(new)):
                        new[index]=str(0)
                    new = ''.join(new)
                    return modify(new,s)
                index-=1
        #return n