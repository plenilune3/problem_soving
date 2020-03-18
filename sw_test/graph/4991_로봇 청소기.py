from collections import deque


def permutations(depth, N, M, visited, room_distance, now=0, result=0):
    global answer

    if result > answer:
        return
    if depth == M:
        answer = min(result, answer)
    else:
        for i in range(N):
            if visited[i] is False:
                visited[i] = True
                result += room_distance[now][i+1]
                permutations(depth+1, N, M, visited, room_distance, i+1, result)
                visited[i] = False
                result -= room_distance[now][i+1]


def bfs(W, H, x, y, p, q, room):
    if (x, y) == (p, q): return 0
    distance = [[-1 for w in range(W)] for h in range(H)]
    queue = deque([(x, y)])
    distance[x][y] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < H and 0 <= ny < W:
                if room[nx][ny] != 'x' and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
                if (nx, ny) == (p, q):
                    return distance[nx][ny]

    return -1


answer = 0

def solution():

    while True:
        W, H = map(int, input().split())

        if W == 0 and H == 0:
            break

        room = [list(input()) for h in range(H)]
        dusts = deque()
        flag = False

        for i in range(H):
            for j in range(W):
                if room[i][j] == 'o':
                    dusts.appendleft((i, j))
                elif room[i][j] == '*':
                    dusts.append((i, j))

        length_dusts = len(dusts)

        room_distance = [[0 for i in range(length_dusts)] for j in range(length_dusts)]

        for i in range(length_dusts):
            x, y = dusts[i]
            for j in range(i+1, length_dusts):
                p, q = dusts[j]
                room_distance[i][j] = bfs(W, H, x, y, p, q, room)
                room_distance[j][i] = room_distance[i][j]
                if room_distance[i][j] == -1:
                    flag = True
                    break
            if flag:
                break

        if flag:
            print(-1)
        else:
            global answer
            answer = float('inf')
            visited = [False for i in range(length_dusts)]
            permutations(0, length_dusts-1, length_dusts-1, visited, room_distance)
            print(answer)


solution()

