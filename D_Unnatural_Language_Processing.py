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
    s = input()
    vowels = {'a','e'}
    converted = ['V' if ch in vowels else 'C' for ch in s]
    converted.reverse()
    l = list(s)
    i = 0
    res = ''
    while i<len(converted):
        if converted[i]=='C':
            for j in range(3):
                res+=l.pop()
            res+='.'
            i+=3
        elif converted[i]=='V':
            for k in range(2):
                res+=l.pop()
            res+='.'
            i+=2
    res = res[::-1]
    print(res[1:])