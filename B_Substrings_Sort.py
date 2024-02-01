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
def substring(string1,string2):
    n1,n2 = len(string1),len(string2)
    if n1>n2:
        return False
    res = False
    for i in range(n2-n1+1):
        if string2[i:i+n1]==string1:
            res = True
    return res

n = int(input())
strings = [0]*n
for i in range(n):
    strings[i] = input()
strings = sorted(strings,key = lambda x:len(x))
#print(strings)
prev = strings[0]
res = True
for s in strings:
    if not substring(prev,s):
        res = False 
        break
    prev = s
    
if res:
    print('YES')
    for s in strings:
        print(s)
else:
    print('NO')    