from heapq import *


def dijkstra(K, N, adjacent):
    prev = [False for i in range(N + 1)]
    distance = [float('inf') for i in range(N + 1)]
    distance[K] = 0

    queue = []
    heappush(queue, [0, K])

    while queue:
        current_distance, current_node = heappop(queue)

        for node_next, length in adjacent[current_node].items():
            distance_next = distance[current_node] + length

            if distance_next < distance[node_next]:
                distance[node_next] = distance_next
                prev[node_next] = current_node
                heappush(queue, [distance_next, node_next])

    return distance


def solution(N, road, K):
    answer = 0
    adjacent = [{} for _ in range(N + 1)]

    for edge in road:
        u, v, w = edge

        if v in adjacent[u]:
            adjacent[u][v] = min(adjacent[u][v], w)
        else:
            adjacent[u][v] = w
        if u in adjacent[v]:
            adjacent[v][u] = min(adjacent[v][u], w)
        else:
            adjacent[v][u] = w

    distance = dijkstra(1, N, adjacent)

    for dist in distance:
        if dist <= K:
            answer += 1

    return answer
