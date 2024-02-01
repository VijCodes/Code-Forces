from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right,insort
from math import sqrt,log10,log2,gcd,inf
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

right = Counter()
rightA = deque([])
left = Counter()
leftA = deque([])
segC = Counter()
for _ in range(int(input())):
    op,l,r = map(str,input().split())
    l,r = int(l),int(r)
    if op == '+':
        segC[(l,r)]+=1
        insort(rightA,r)
        insort(leftA,l)
        while leftA and left[leftA[-1]]:
            left[leftA[-1]]-=1
            leftA.pop()
        if leftA:
            maxLeft = leftA[-1]
        else:
            maxLeft = -inf
        while rightA and right[rightA[0]]:
            right[rightA[0]]-=1
            rightA.popleft()
        if rightA:
            minRight = rightA[0]
        else:
            minRight = inf
        if minRight<maxLeft:
            print('YES')
        else:
            print('NO')
    else:
        segC[(l,r)]-=1
        left[l]+=1
        right[r]+=1
        while leftA and left[leftA[-1]]:
            left[leftA[-1]]-=1
            leftA.pop()
        if leftA:
            maxLeft = leftA[-1]
        else:
            maxLeft = -inf
        while rightA and right[rightA[0]]:
            right[rightA[0]]-=1
            rightA.popleft()
        if rightA:
            minRight = rightA[0]
        else:
            minRight = inf
        if minRight<maxLeft:
            print('YES')
        else:
            print('NO')
        
            
        
            
    
    