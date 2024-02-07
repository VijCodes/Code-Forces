from sys import stdin
input = lambda: stdin.buffer.readline().decode().strip()
#import sys
#sys.setrecursionlimit(10000)
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())


n = int(input())
a = list(map(int,input().split()))
res = 0
MOD = 998244353
for i in range(32):
    odds, evens, odd_l, even_l = [0]*4
    for j, val in enumerate(a):
        if (1 << i) & val:
            odd_l, even_l = even_l + evens + 1, odd_l + odds
            odds, evens = evens, odds
            odds += 1            
        else:
            even_l, odd_l = even_l + evens + 1, odd_l + odds
            evens += 1
        #print(i, odd_l, even_l, odds, evens)
        res = ( res + odd_l * (1 << i) ) % MOD
print(res)