
def solution(N, S, M, volumes):
    answer = -1
    dp = [[False for i in range(M+1)] for j in range(N+1)]
    volumes = [0] + volumes
    dp[0][S] = True

    for i in range(1, N+1):
        for j in range(M+1):
            if dp[i-1][j] is False:
                continue
            if j - volumes[i] >= 0:
                dp[i][j-volumes[i]] = True
            if j + volumes[i] <= M:
                dp[i][j+volumes[i]] = True

    for i in range(M, -1, -1):
        if dp[N][i]:
            answer = i
            break

    print(answer)


N, S, M = map(int, input().split())
volumes = list(map(int, input().split()))

solution(N, S, M, volumes)
