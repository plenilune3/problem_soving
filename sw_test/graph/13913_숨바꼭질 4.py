from collections import deque


def bfs(N, K):
    distance = [0 for i in range(100001)]
    path = [0 for i in range(100001)]
    queue = deque([N])

    if N > K:
        return N - K, [N - i for i in range(N - K + 1)]

    while queue:
        node = queue.popleft()
        if node == K:
            route = []
            while node != N:
                route.append(node)
                node = path[node]
            route.append(node)
            route.reverse()
            return distance[K], route
        else:
            if node - 1 >= 0 and distance[node - 1] == 0:
                distance[node - 1] = distance[node] + 1
                path[node - 1] = node
                queue.append(node - 1)
            if node + 1 <= K + 1 and distance[node + 1] == 0:
                distance[node + 1] = distance[node] + 1
                path[node + 1] = node
                queue.append(node + 1)
            if node * 2 <= K + 1 and distance[node * 2] == 0:
                distance[node * 2] = distance[node] + 1
                path[node * 2] = node
                queue.append(node * 2)


def solution():

    N, K = map(int, input().split())
    answer, route = bfs(N, K)

    print(answer)
    print(' '.join(map(str, route)))


solution()

