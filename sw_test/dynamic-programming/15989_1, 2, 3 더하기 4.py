
def solution():
    dp = [[0, 1, 0, 0] for i in range(10001)]
    dp[1] = [0, 1, 0, 0]
    dp[2] = [0, 1, 1, 0]
    dp[3] = [0, 1, 1, 1]

    for i in range(4, 10001):
        dp[i][2] = dp[i-2][1] + dp[i-2][2]
        dp[i][3] = dp[i-3][1] + dp[i-3][2] + dp[i-3][3]

    return dp


dp = solution()
T = int(input())

for t in range(T):
    N = int(input())
    answer = sum(dp[N])
    print(answer)
