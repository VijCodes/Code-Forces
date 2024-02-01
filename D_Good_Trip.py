MOD = 1000000007
N = 200005

fact = [1] * N  # Factorial precomputation array
inv = [1] * N  # Modular inverse of factorial precomputation array

def power(a, b, p):
    result = 1
    a %= p
    while b > 0:
        if b & 1:
            result = (result * a) % p
        a = (a * a) % p
        b >>= 1
    return result

def precompute():
    for i in range(1, N):
        fact[i] = (i * fact[i - 1]) % MOD
        inv[i] = power(fact[i], MOD - 2, MOD)

def nCr(n, r, p):
    if r > n or r < 0:
        return 0
    if n == r:
        return 1
    if r == 0:
        return 1
    return (((fact[n] * inv[r]) % p) * inv[n - r]) % p

precompute()  # Precompute factorials and their inverses

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    sum_f = 0
    for _ in range(m):
        a, b, f = map(int, input().split())
        sum_f = (sum_f + f) % MOD
    
    den = ((n * (n - 1)) // 2) % MOD
    den_inv = power(den, MOD - 2, MOD)
    base = ((sum_f * k) % MOD) * den_inv % MOD
    avg_inc = 0

    for i in range(1, k + 1):
        sum_i = ((i * (i - 1)) // 2) % MOD
        prob = (nCr(k, i, MOD) * power(den_inv, i, MOD)) % MOD
        unpicked_prob = ((den - 1) * den_inv) % MOD
        prob = (prob * power(unpicked_prob, k - i, MOD)) % MOD
        avg_inc = (avg_inc + (sum_i * prob) % MOD) % MOD
    
    ans = (base + (m * avg_inc) % MOD) % MOD
    print(ans)
