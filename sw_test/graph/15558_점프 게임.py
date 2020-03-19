from collections import deque


def bfs(N, K, board):
    visited = [[False for i in range(N)] for j in range(2)]
    queue = [(0, 0)]
    visited[0][0] = True
    count = 0

    while queue:
        cases = []

        for x, y in queue:
            if board[x][y] == 1:
                nx, ny = x, y+1
                if ny > N-1:
                    return 1
                else:
                    if visited[nx][ny] is False and board[nx][ny] == 1:
                        visited[nx][ny] = True
                        cases.append((nx, ny))

                nx, ny = (x + 1) % 2, y + K
                if ny > N-1:
                    return 1
                else:
                    if visited[nx][ny] is False and board[nx][ny] == 1:
                        visited[nx][ny] = True
                        cases.append((nx, ny))

                nx, ny = x, y-1
                if ny < 0:
                    pass
                else:
                    if visited[nx][ny] is False and board[nx][ny] == 1:
                        visited[nx][ny] = True
                        cases.append((nx, ny))

        board[0][count] = 0
        board[1][count] = 0
        queue = cases
        count += 1

    return 0


def solution(N, K):
    board = [list(map(int, input())), list(map(int, input()))]

    answer = bfs(N, K, board)
    print(answer)


N, K = map(int, input().split())

solution(N, K)


# def bfs(N, K, board):
#     visited = [[False for i in range(N)] for j in range(2)]
#     visited[0][0] = True
#     queue = deque([(0, 0)])
#     count = 0
#
#     while queue:
#         cases = []
#
#         for x, y in queue:
#             if board[x][y] == '1':
#                 for nx, ny in [(x, y-1), (x, y+1), (not x, y+K)]:
#                     if ny > N-1:
#                         return 1
#                     elif ny >= 0 and visited[nx][ny] is False:
#                         visited[nx][ny] = True
#                         cases.append((nx, ny))
#
#         board[0][count] = '0'
#         board[1][count] = '0'
#         queue = cases
#         count += 1
#
#     return 0
#
#
# def solution(N, K):
#     board = [list(input()), list(input())]
#     answer = bfs(N, K, board)
#     print(answer)
#
#
# N, K = map(int, input().split())
#
# solution(N, K)
#