from collections import deque


def move(W, H, x, y, dx, dy, queue, visited, board):
    temp = visited[x][y]

    while 0 <= x + dx < H and 0 <= y + dy < W and board[x + dx][y + dy] != '*':
        if visited[x + dx][y + dy] == -1:
            visited[x + dx][y + dy] = temp + 1
            queue.append((x + dx, y + dy))
        x += dx
        y += dy


def bfs(W, H, x, y, fx, fy, board):
    visited = [[-1 for w in range(W)] for h in range(H)]
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

