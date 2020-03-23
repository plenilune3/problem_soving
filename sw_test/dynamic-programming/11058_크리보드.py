def solution(N):
    dp = [0 for i in range(101)]
    dp[1], dp[2], dp[3] = 1, 2, 3

    for i in range(4, N+1):
        dp[i] = max(dp[i], dp[i-1] + 1)
        for j in range(3, i):
            dp[i] = max(dp[i], dp[i-j] * (j-1))

    print(dp[N])


N = int(input())
solution(N)
