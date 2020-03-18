from collections import deque


def bfs(N):
    visited = [False for i in range(N)]
    prev = [-1 for i in range(N)]
    how = [-1 for i in range(N)]
    queue = deque([1])
    visited[1] = True
    how[1] = 1

    while queue:
        now = queue.popleft()
        for i in range(2):
            next_ = (now * 10 + i) % N
            if visited[next_] is False:
                visited[next_] = True
                prev[next_] = now
                how[next_] = i
                queue.append(next_)

    if visited[0] is False:
        return 'BRAK'
    else:
        answer = ''
        now = 0
        while now != -1:
            answer = str(how[now]) + answer
            now = prev[now]
        return answer


def solution(N):
    if N == 1:
        print(1)
    else:
        answer = bfs(N)
        print(answer)


T = int(input())

for t in range(T):
    N = int(input())
    solution(N)

