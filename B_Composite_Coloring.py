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
    n = int(input())
    a = list(map(int,input().split()))
    primes = [2,3,5,7,11,13,17,19,23,29,31]
    num_to_color = defaultdict(int)
    
    def least_prime(val):
        for p in primes:
            if val%p==0:
                return p
            
    primes_new = set()
    for val in a:
        primes_new.add(least_prime(val))
    
    for i,val in enumerate(list(primes_new)):
        num_to_color[val] = i+1
    #print(num_to_color)
    res = list(map(lambda x:num_to_color[least_prime(x)], a))
    print(len(primes_new))
    print(*res)