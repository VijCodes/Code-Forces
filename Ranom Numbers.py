# **** Packages **** #
 
from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
 
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())

for _ in range(int(input())):
    ranom = input()
    counter = Counter() # counts the chars seen in the first loop
    lastIndex = defaultdict(lambda:-1)
    dp = [-1]*len(ranom) # lets -1 means there is no greater element to the right # -2 means there are more than 2 greater elements to the right
    alp = ['A','B','C','D','E']
    ranomL = list(ranom[::-1])
    for i,char in enumerate(ranomL):
        greater = 0 # number of greater characters seen until now
        for chr in alp:
            if chr>char:
                greater+=counter[chr]
                if counter[chr]:
                    chrG = chr
        counter[char]+=1
        if greater >= 2:
            dp[i] = -2
        elif greater == 1:
            dp[i] = lastIndex[chrG]
        else:
            dp[i] = -1
        lastIndex[char] = i
    print(lastIndex)
    print(dp)
    res = 0
    gCounter = Counter()
    delta = [defaultdict(int)]*len(ranomL) # when value is reduced to less than or equal to character then we +delta[i][char] 
    curr = 0
    maxDelta = 0
    for i in reversed(range(len(ranomL))):
        for ch in alp:
            maxDelta = max(maxDelta,delta[i][ch]+gCounter[ch]+(10**(ord(ch)-ord('A')))-(10**(ord(char)-ord('A')))) 
        char = ranomL[i]
        ind = dp[i]
        if ind == -1:
            for ch in alp:
                if ch>char:
                    gCounter[ch]-=2*(10**(ord(char)-ord('A')))
            curr+=10**(ord(char)-ord('A'))
        elif ind == -2:
            curr-=10**(ord(char)-ord('A'))
        else:
            curr-=10**(ord(char)-ord('A'))
            for ch in alp:
                if ch<=char:
                    delta[ind][ch]+=2*(10**(ord(char)-ord('A')))
    print(curr+maxDelta)
       

            