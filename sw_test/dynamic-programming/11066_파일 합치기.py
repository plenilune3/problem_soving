def solution(K, chapters):
    dp = [[0 for i in range(K)] for j in range(K)]

    for i in range(K-1):
        dp[i][i+1] = chapters[i] + chapters[i+1]
        for j in range(i+2, K):
            dp[i][j] = dp[i][j-1] + chapters[j]

    for diff in range(2, K):
        for i in range(K-diff):
            j = i + diff
            minimum = [dp[i][k] + dp[k+1][j] for k in range(i, j)]
            dp[i][j] += min(minimum)

    return dp[0][K-1]


T = int(input())

for t in range(T):
    K = int(input())
    chapters = list(map(int, input().split()))

    answer = solution(K, chapters)

    print(answer)
