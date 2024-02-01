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

st = input()
n = len(st)
valToInd = defaultdict(list)
for i,val in enumerate(list(st)):
    if int(val)==0:
        valToInd[0].append(n-i)
    else:
        valToInd[int(val)] = [n-i]
def update(ind1,ind2):
    lz = 0
    result = inf
    for i,s in enumerate(st):
        if i in (n-ind1,n-ind2):
            continue
        elif int(s)!=0:
            result = lz
            break
        else:
            lz+=1
    if lz==0: #handle the case where there are no zeros at all and no additional numbers
        result = 0
    if ind2>ind1:
        swaps = ind2+ind1-3
    else:
        swaps = ind2+ind1-2
    return swaps+result
#print(valToInd)
res = inf
# 00
if 0 in valToInd and len(valToInd[0])>=2:
    ind2,ind1 = valToInd[0][-1],valToInd[0][-2]
    swaps = ind2+ind1-3
    res = min(swaps,res)
# 25
if 2 in valToInd and 5 in valToInd:
    ind2,ind1 = valToInd[2][-1],valToInd[5][-1]
    swaps = update(ind1,ind2)
    res = min(res,swaps)
# 50 
if 5 in valToInd and 0 in valToInd:
    ind2,ind1 = valToInd[5][-1],valToInd[0][-1]
    swaps = update(ind1,ind2)
    res = min(res,swaps)
# 75
if 7 in valToInd and 5 in valToInd:
    ind2,ind1 = valToInd[7][-1],valToInd[5][-1]
    swaps = update(ind1,ind2)
    res = min(res,swaps)
print(res if res!=inf else -1)

