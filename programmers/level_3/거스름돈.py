def solution(n, money):
    dp = [0 for i in range(n+1)]
    dp[0] = 1

    for m in money:
        for i in range(1, n+1):
            if i >= m:
                dp[i] = dp[i-m] + dp[i]

    answer = dp[-1]
    return answer
