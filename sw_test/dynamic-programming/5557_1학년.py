
def solution(N, numbers):
    dp = [[0 for i in range(21)] for j in range(N)]
    dp[1][numbers[0]] = 1

    for i in range(1, N):
        for j in range(21):
            if dp[i-1][j] == 0:
                continue
            if j - numbers[i-1] >= 0:
                dp[i][j-numbers[i-1]] += dp[i-1][j]
            if j + numbers[i-1] <= 20:
                dp[i][j+numbers[i-1]] += dp[i-1][j]

    # print(*dp, sep='\n')
    print(dp[-1][numbers[-1]])


N = int(input())
numbers = list(map(int, input().split()))
solution(N, numbers)
