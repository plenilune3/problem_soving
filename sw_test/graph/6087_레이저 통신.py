from collections import deque


def move(W, H, x, y, dx, dy, queue, visited, board):
    nx, ny = x + dx, y + dy

    while 0 <= nx < H and 0 <= ny < W and board[nx][ny] != '*':
        # 이미 지나온 경로지만 거울이 더 필요하면 넘어감
        if visited[nx][ny] < visited[x][y] + 1:
            break

        visited[nx][ny] = visited[x][y] + 1
        queue.append((nx, ny))
        nx = nx + dx
        ny = ny + dy


def bfs(W, H, x, y, fx, fy, board):
    visited = [[float('inf') for w in range(W)] for h in range(H)]
    queue = deque([(x, y)])
    visited[x][y] = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        if (x, y) == (fx, fy):
            return visited[x][y] - 1

        for i in range(4):
            move(W, H, x, y, dx[i], dy[i], queue, visited, board)


W, H = map(int, input().split())
board = [list(input()) for h in range(H)]


def solution(W, H, board):
    C = []
    for i in range(H):
        for j in range(W):
            if board[i][j] == 'C':
                C.append((i, j))

    x, y = C[0]
    fx, fy = C[1]

    answer = bfs(W, H, x, y, fx, fy, board)
    print(answer)


solution(W, H, board)

