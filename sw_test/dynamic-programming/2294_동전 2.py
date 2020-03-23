

def solution(N, K, coins):
    dp = [100001 for i in range(K+1)]
    dp[0] = 0

    for coin in coins:
        for j in range(1, K+1):
            if j >= coin:
                dp[j] = min(dp[j-coin] + 1, dp[j])

    print(dp[K] if dp[K] != 100001 else -1)


N, K = map(int, input().split())
coins = [int(input()) for i in range(N)]

solution(N, K, coins)
