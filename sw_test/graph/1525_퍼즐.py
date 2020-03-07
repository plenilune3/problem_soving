from collections import deque


def bfs(state: str):
    visited = {state: 0}
    queue = deque([state])
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    while queue:
        state = queue.popleft()
        if state == '123456780':
            return visited[state]
        else:
            k: int = state.find('0')
            x, y = k // 3, k % 3
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < 3 and 0 <= ny < 3:
                    nk = nx * 3 + ny
                    state_list = list(state)
                    state_list[k], state_list[nk] = state_list[nk], state_list[k]
                    state_next = ''.join(state_list)
                    if visited.get(state_next) is None:
                        visited[state_next] = visited[state] + 1
                        queue.append(state_next)
    return -1


def solution():
    board = [input().split() for i in range(3)]

    state = ''
    for i in range(3):
        for j in range(3):
            state += board[i][j]

    answer = bfs(state)
    print(answer)


solution()
