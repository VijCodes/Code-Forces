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
    t = input()
    next_letter = dict()
    past_letter = dict()
    poss = [chr(val+ord('a')) for val in range(26)]
    res = ['a']*n
    for i, ch in enumerate(list(t)):
        if ch in next_letter:
            res[i] = next_letter[ch]     
        else:
            collect = set()
            collect.add(ch)
            start = ch
            while start in past_letter and past_letter[start] not in collect:
                collect.add(past_letter[start])
                start = past_letter[start]
            for nex_l in poss:
                if nex_l not in past_letter and nex_l not in collect:
                    break
            if len(collect)==26:
                nex_l = start
            next_letter[ch] = nex_l
            past_letter[nex_l] = ch
            res[i] = nex_l
    print(''.join(res))