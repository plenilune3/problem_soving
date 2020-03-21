def solution(N, board):
    dp = [[0 for i in range(N)] for j in range(N)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                continue
            if board[i][j] + i < N:
                dp[board[i][j] + i][j] += dp[i][j]
            if board[i][j] + j < N:
                dp[i][board[i][j] + j] += dp[i][j]

    print(dp[N-1][N-1])


N = int(input())
board = [list(map(int, input().split())) for n in range(N)]


solution(N, board)
