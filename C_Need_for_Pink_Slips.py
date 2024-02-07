from functools import cache  # Only import cache, as it's the one used
from sys import stdin

input = lambda: stdin.buffer.readline().decode().strip()

for _ in range(int(input())):
    c, m, p, v = map(float, input().split())

    @cache
    def Expected(c, m, p, v):
        # Adjusted base case to account for current probability of drawing a Pink Slip
        if c < 1e-9 and m < 1e-9:  # Using a small threshold for floating-point comparison
            return 1
        res = p
        if c > 1e-9:  # Using a small threshold for floating-point comparison
            delta = min(c, v)
            if m < 1e-9:  # Using a small threshold for floating-point comparison
                res += c * (1 + Expected(c - delta, 0, p + delta, v))
            else:
                res += c * (1 + Expected(c - delta, m + delta / 2, p + delta / 2, v))
        if m > 1e-9:  # Using a small threshold for floating-point comparison
            delta = min(m, v)
            if c < 1e-9:  # Using a small threshold for floating-point comparison
                res += m * (1 + Expected(0, m - delta, p + delta, v))
            else:
                res += m * (1 + Expected(c + delta / 2, m - delta, p + delta / 2, v))
        return res

    print(Expected(c, m, p, v))
