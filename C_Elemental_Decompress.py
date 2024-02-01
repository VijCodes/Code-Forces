from functools import lru_cache
from itertools import permutations, combinations, product, accumulate, cycle, chain
from collections import defaultdict,deque, Counter
from bisect import bisect,bisect_left,bisect_right
from math import sqrt,log10,log2,gcd,inf
 
##### ***** Frequently Used Code ***** #######
# list(map(int,input().split()))
# int(input())
for _ in range(int(input())):
    n =int(input())
    a = list(map(int,input().split()))
    c = Counter(a)
    indexes = defaultdict(list)
    for i,a in enumerate(a):
        indexes[a].append(i)
    array = deque([])
    p = [1]*n
    q = [1]*n
    res = 0
    for i in reversed(range(1,n+1)):
        if c[i]==2:
            array.append(i)
        elif c[i]==0:
            array.appendleft(i)
        elif c[i]==1:
            ind = indexes[i][0]
            p[ind] = i
            q[ind] = i
        else:
            res = 1
    if res:
        print('NO')
        continue
    while array:
        f = array.popleft()
        s = array.pop()
        ind1,ind2 = indexes[s]
        if f>s:
            res = 1
            break
        p[ind1],p[ind2]=s,f
        q[ind1],q[ind2]=f,s 
    if res:
        print('NO')
    else:
        print('YES')
        print(' '.join(map(str,p)))
        print(' '.join(map(str,q)))