from collections import deque


def bfs(H: int, W: int, keys: list, floor_plan: list):
    visited = [[False for i in range(W+2)] for j in range(H+2)]
    doors = [[] for i in range(26)]
    answer = 0
    queue = deque([(0, 0)])
    visited[0][0] = True
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < H+2 and 0 <= ny < W+2:
                if floor_plan[nx][ny] == '*' or visited[nx][ny] is True:
                    continue
                visited[nx][ny] = True
                if floor_plan[nx][ny] == '$':
                    answer += 1
                elif 'A' <= floor_plan[nx][ny] <= 'Z':
                    door = ord(floor_plan[nx][ny]) - ord('A')
                    if keys[door] is False:
                        doors[door].append((nx, ny))
                        continue
                elif 'a' <= floor_plan[nx][ny] <= 'z':
                    key = ord(floor_plan[nx][ny]) - ord('a')
                    keys[key] = True
                    for door in doors[key]:
                        kx, ky = door
                        queue.append((kx, ky))
                queue.append((nx, ny))

    return answer


def solution():
    T = int(input())

    for t in range(T):
        H, W = map(int, input().split())

        floor_plan = [['.' for w in range(W+2)]]
        for h in range(H):
            floor_plan.append(list('.' + input() + '.'))
        floor_plan.append(['.' for w in range(W+2)])

        keys = [False for i in range(26)]
        k = input()
        if k != '0':
            for t in k:
                keys[ord(t) - ord('a')] = True

        answer = bfs(H, W, keys, floor_plan)
        print(answer)


solution()

