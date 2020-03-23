def solution(N, K, coins):
    dp = [0 for i in range(K+1)]
    dp[0] = 1

    for coin in coins:
        for j in range(1, K+1):
            if j >= coin:
                dp[j] += dp[j-coin]

    print(dp[K])


N, K = map(int, input().split())
coins = [int(input()) for i in range(N)]

solution(N, K, coins)
