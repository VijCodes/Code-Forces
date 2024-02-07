for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0]*4
    dp[1] = a[0]
 
    for i in range(1, n):
        dp[3] = max(dp[3], dp[2] + a[i] - i)
        dp[2] = max(dp[2], dp[1] + a[i])
        dp[1] = max(dp[1], dp[0] + a[i] + i)
 
    print(dp[3])