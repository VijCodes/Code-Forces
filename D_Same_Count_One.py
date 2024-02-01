from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain,groupby
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
for _ in range(int(input())):
    rows,cols = map(int,input().split())
    mat = []
    total = 0
    rowCnt = [0]*rows
    for r in range(rows):
        lst = list(map(int,input().split()))
        rowCnt[r] = sum(lst)
        total+=rowCnt[r]
        mat.append(lst)
    if total%rows!=0:
        print(-1)
    else:
        perRow = total//rows
        swaps = sum([max(0,val-perRow) for val in rowCnt])
        print(swaps)
        for c in range(cols):
            pos = []
            neg = []
            for r in range(rows):
                if rowCnt[r]>perRow and mat[r][c]==1:
                    pos.append(r)
                elif rowCnt[r]<perRow and mat[r][c]==0:
                    neg.append(r)
            while pos and neg:
                rowCnt[pos[-1]]-=1
                rowCnt[neg[-1]]+=1
                print(str(pos.pop()+1)+' '+str(neg.pop()+1)+' '+str(c+1))
    