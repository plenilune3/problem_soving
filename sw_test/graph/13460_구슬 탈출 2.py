from collections import deque


def init(board, N, M):
    rx, ry, bx, by = [0, 0, 0, 0]

    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j

    return rx, ry, bx, by


def move(x, y, dx, dy, move_count, board):
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        move_count += 1
    return x, y, move_count


def bfs(rx, ry, bx, by, visited, board):
    dx, dy = (0, 0, -1, 1), (-1, 1, 0, 0)
    queue = deque([(rx, ry, bx, by, 0)])
    visited[rx][ry][bx][by] = True

    while queue:
        rx, ry, bx, by, count = queue.popleft()
        if count >= 10:
            break
        else:
            for i in range(4):
                nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0, board)
                nbx, nby, bc = move(bx, by, dx[i], dy[i], 0, board)
                if board[nbx][nby] == 'O':
                    continue
                if board[nrx][nry] == 'O':
                    return count + 1
                if nrx == nbx and nry == nby:
                    if rc > bc:
                        nrx, nry = nrx-dx[i], nry-dy[i]
                    else:
                        nbx, nby = nbx-dx[i], nby-dy[i]
                if visited[nrx][nry][nbx][nby] is False:
                    visited[nrx][nry][nbx][nby] = True
                    queue.append((nrx, nry, nbx, nby, count+1))
    return -1



def solution():
    N, M = map(int, input().split())
    board = [list(input()) for i in range(N)]
    visited = [[[[False for i in range(M)] for j in range(N)] for p in range(M)] for q in range(N)]
    rx, ry, bx, by = init(board, N, M)

    answer = bfs(rx, ry, bx, by, visited, board)
    print(answer)


solution()
