from collections import deque


def bfs(x, y, W, H, floor_plan):
    distance = [[-1 for w in range(W+2)] for h in range(H+2)]
    queue = deque([(x, y)])
    distance[x][y] = 0

    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx > H+1 or ny < 0 or ny > W+1:
                continue
            if distance[nx][ny] >= 0 or floor_plan[nx][ny] == '*':
                continue
            if floor_plan[nx][ny] == '.':
                distance[nx][ny] = distance[x][y]
                queue.appendleft((nx, ny))
            elif floor_plan[nx][ny] == '#':
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

    return distance


def solution():
    T = int(input())

    for t in range(T):
        H, W = map(int, input().split())
        queue = []

        floor_plan = [['.' for w in range(W+2)]]
        for h in range(H):
            floor_plan.append(list('.' + input() + '.'))
        floor_plan.append(['.' for w in range(W+2)])

        for i in range(H+2):
            for j in range(W+2):
                if floor_plan[i][j] == '$':
                    floor_plan[i][j] = '.'
                    queue.append((i, j))

        x, y = queue.pop()
        distance1 = bfs(x, y, W, H, floor_plan)
        x, y = queue.pop()
        distance2 = bfs(x, y, W, H, floor_plan)
        distance3 = bfs(0, 0, W, H, floor_plan)
        answer = 10000

        for i in range(H+2):
            for j in range(W+2):
                if floor_plan[i][j] != '*':
                    k = distance1[i][j] + distance2[i][j] + distance3[i][j]
                    if floor_plan[i][j] == '#':
                        k -= 2
                    answer = min(k, answer)

        print(answer)


solution()

