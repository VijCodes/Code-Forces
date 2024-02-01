from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf,perm,comb,ceil,floor
from sys import stdin,stdout
input = lambda: stdin.buffer.readline().decode().strip()
from heapq import heapify,heappop,heappush,heapreplace

for _ in range(int(input())):
    X = int(input())
    def find_group_sizes(X):
        """ Finds group sizes such that the sum of 2^group_size - 1 equals X - 1 """
        group_sizes = []
        remaining = X - 1  # Subtracting 1 for the empty subsequence

        while remaining > 0:
            # Find the largest power of 2 less than or equal to remaining
            m = remaining.bit_length() - 1
            group_sizes.append(m + 1)  # Add 1 because groups are 1-indexed
            remaining -= (2 ** m - 1)

        return group_sizes

    def construct_array(group_sizes):
        """ Constructs the array from group sizes """
        array = []
        current_start = 1
        for size in group_sizes:
            array.extend(range(current_start, current_start + size))
            current_start += size
        return len(array), array
    
    groups = find_group_sizes(X)
    ans1,ans2 = construct_array(groups)
    print(ans1)
    print(*ans2)
    