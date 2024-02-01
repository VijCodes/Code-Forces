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

n = int(input())
x = list(map(int,input().split()))
s = defaultdict(lambda:defaultdict(lambda:1))
x.sort(reverse=True)

for val in x:
    i = 0
    res = 1
    ans = 1
    s[val] = defaultdict(lambda:1)
    while val+2**i<=10**9:
        if (val+2**i) in s:
            s[val][i]=1+s[val+2**i][i]
            if s[val][i]>ans:
                res = [val,i]
                ans = s[val][i]
        i+=1
    if ans==3:
        break
    
if ans==1:
    print(1)
    print(x[0])
elif ans==2:
    val,i = res
    res = [val,val+2**i]
    print(2)
    print(' '.join(map(str,res)))
elif ans==3:
    val,i = res
    res = [val,val+2**i,val+2**(i+1)]
    print(3)
    print(' '.join(map(str,res)))

