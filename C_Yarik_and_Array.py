from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
 
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    stackMin = 0
    #pSum = [0]+accumulate(a)
    currSum = 0
    res = -inf
    prev = a[0]+1
    for val in a:
        if val%2==prev%2:
            currSum = 0
            stackMin = 0
        currSum+=val
        prev = val
        res = max(res,currSum-stackMin)
        stackMin = min(currSum,stackMin)
    print(res)
        