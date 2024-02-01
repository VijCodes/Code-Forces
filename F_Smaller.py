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
    q = int(input())
    sCnt = defaultdict(int)
    tCnt = defaultdict(int)
    sCnt['a']+=1
    tCnt['a']+=1
    sSmall = 'a'
    tLarge = 'a'
    totalS = 1
    totalT = 1
    for _ in range(q):
        d,k,x = map(str,input().split())  
        d,k = int(d),int(k)
        if d==1:
            totalS+=k*len(x)
            for ch in x:
                sSmall = min(sSmall,ch)
                sCnt[ch]+=k
        else:
            totalT+=k*len(x)
            for ch in x:
                tLarge = max(tLarge,ch)
                tCnt[ch]+=k
        #print(sSmall,tLarge)
        if not totalS and totalT:
            print('YES')
        elif not totalT and totalS:
            print('NO')
        elif sSmall<tLarge:
            print('YES')
        elif sSmall>tLarge:
            print('NO')
        else:
            if tCnt[tLarge]<sCnt[sSmall]:
                print('NO')
            elif tCnt[tLarge]>sCnt[sSmall]:
                if totalS-sCnt[sSmall]:
                    print('NO')
                else:
                    print('YES')
            else:
                if totalS==sCnt[sSmall] and totalT-tCnt[tLarge]:
                    print('YES')
                else:
                    print('NO')
            
            