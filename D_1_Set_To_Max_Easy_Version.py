from sys import stdin
input = lambda: stdin.buffer.readline().decode().strip()
from collections import deque
 
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
 
    def solve(order):
        dq = deque()
        for i in order:
            while dq and dq[-1] <= a[i]: dq.pop()
            while dq and dq[0] > b[i]: dq.popleft()
            dq.append(a[i])
            if dq[0] == b[i]: a[i] = b[i]
 
    solve(range(n))
    solve(reversed(range(n)))
    print('YES' if a == b else 'NO')