N, M = map(int, input().split())
maze = [[0 for m in range(M+1)]]
for n in range(N):
    maze.append([0] + list(map(int, input().split())))


def solution(N, M, maze):
    for x in range(1, N+1):
        for y in range(1, M+1):
            maze[x][y] = maze[x][y] + max(maze[x-1][y], maze[x][y-1])
    print(maze[N][M])


solution(N, M, maze)
