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
for _ in range(int(input())):
    n = int(input())
    s = input()
    sl = list(map(lambda x:ord(x)-ord('a'),list(s)))
    greatest = -inf
    largSeq = []
    add = [0]*n
    for i in reversed(range(n)):
        greatest = max(greatest,sl[i])
        if greatest==sl[i]:
            largSeq.append(sl[i])
            add[i] = 1
    largSeq.sort(reverse = True)
    c = Counter(largSeq)
    operations = sum(add)-c[largSeq[0]]
    final = []
    for i,val in enumerate(sl):
        if add[i]:
            final.append(largSeq.pop())
        else:
            final.append(sl[i])
    if final==sorted(sl):
        print(operations)
    else:
        print(-1)
        
    
    
        