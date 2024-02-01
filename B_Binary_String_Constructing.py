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

a,b,x = map(int,input().split())
if x==0 or x==1:
    res = '0'*a + '1'*b
    print(res)
else:
    mini = min(a,b)
    if x%2:
        gps = ceil(x/2)
        zeroA = ['0']*gps
        oneA = ['1']*gps
        zeroA[0] = '0'*(a-gps+1)
        oneA[0] = '1'*(b-gps+1)
        res = ''
        while zeroA or oneA:
            if oneA:
                res+=oneA.pop()
            if zeroA:
                res+=zeroA.pop()
        print(res)
    else:
        gps = x//2
        if a<b:
            zeroA = ['0']*gps
            oneA = ['1']*(gps+1)
            zeroA[0] = '0'*(a-gps+1)
            oneA[0] = '1'*(b-gps)
            res = ''
            while zeroA or oneA:
                if oneA:
                    res+=oneA.pop()
                if zeroA:
                    res+=zeroA.pop()
            print(res)
        elif b<=a:
            zeroA = ['0']*(gps+1)
            oneA = ['1']*gps
            zeroA[0] = '0'*(a-gps)
            oneA[0] = '1'*(b-gps+1)
            res = ''
            while zeroA or oneA:
                if zeroA:
                    res+=zeroA.pop()
                if oneA:
                    res+=oneA.pop()
            print(res)
    
        
        
        
    