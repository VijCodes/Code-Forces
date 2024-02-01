from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb

#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ai = sorted([(val,i) for i,val in enumerate(a)])
    pref = [0] 
    for val,index in ai:
        pref.append(pref[-1]+val)
    res = [1]*n
    for i in reversed(range(n)):
        val,ind = ai[i]
        if i==n-1:
            res[ind]= n-1
        elif pref[i+1]>=ai[i+1][0]:
            res[ind] = res[ai[i+1][1]]
        else:
            res[ind] = i
    print(' '.join(map(str,res)))
        
     