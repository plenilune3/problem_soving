N, M = map(int, input().split())
paper = [list(map(int, input())) for i in range(N)]
visited = [[False for i in range(M)] for j in range(N)]
answer = 0


def calculate():
    sum_total = 0
    sum_temp = 0

    for i in range(N):
        for j in range(M):
            if visited[i][j] is True:
                sum_temp = (sum_temp * 10) + paper[i][j]
            else:
                sum_total += sum_temp
                sum_temp = 0
        sum_total += sum_temp
        sum_temp = 0
    for j in range(M):
        for i in range(N):
            if visited[i][j] is False:
                sum_temp = (sum_temp * 10) + paper[i][j]
            else:
                sum_total += sum_temp
                sum_temp = 0
        sum_total += sum_temp
        sum_temp = 0
    return sum_total


def backtracking(depth, y, x):
    global answer

    if y == N:
        answer = max(answer, calculate())
        return
    if x == M:
        backtracking(depth+1, y+1, 0)
        return
    visited[y][x] = True
    backtracking(depth+1, y, x+1)
    visited[y][x] = False
    backtracking(depth+1, y, x+1)


backtracking(0, 0, 0)
print(answer)
