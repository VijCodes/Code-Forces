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


class FenwickTree:
    def __init__(self, size):
        self.bit = [0] * size

    def update(self, idx, delta):
        while idx < len(self.bit):
            self.bit[idx] += delta
            idx |= idx + 1

    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.bit[idx - 1]
            idx &= idx - 1
        return res

def count_ge_elements(arr):
    # Coordinate compression
    sorted_arr = sorted(set(arr))
    idx_map = {val: idx for idx, val in enumerate(sorted_arr)}

    # Fenwick Tree for frequency counting
    ft = FenwickTree(len(sorted_arr))
    res = 0

    for num in arr:
        # Map the number to its compressed index
        idx = idx_map[num]
        # Count elements greater than or equal to the current element
        res += ft.query(len(sorted_arr)) - ft.query(idx)
        # Update the frequency
        ft.update(idx, 1)
    return res

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    print(count_ge_elements(a))
        