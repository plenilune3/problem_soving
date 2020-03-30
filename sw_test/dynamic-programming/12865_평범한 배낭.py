# def solution(N, K, items):
#     dp = [[0 for i in range(K+1)] for j in range(N+1)]
#
#     for i in range(1, N+1):
#         weight, value = items[i-1]
#         for j in range(1, K+1):
#             if weight <= j:
#                 dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
#             else:
#                 dp[i][j] = dp[i-1][j]
#
#     print(dp[N][K])


def solution(N, K, items):
    dp = [0 for i in range(K+1)]

    for i in range(N):
        weight, value = items[i]
        for j in range(K, 1, -1):
            if weight <= j:
                dp[j] = max(dp[j], dp[j-weight] + value)

    print(dp[-1])


N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for i in range(N)]

solution(N, K, items)
