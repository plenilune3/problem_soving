from collections import deque


def bfs(N, K):
    visited = [False for i in range(100001)]
    queue = [N]
    depth = 0
    count = 0

    if N >= K:
        return N-K, 1

    while queue:
        cases = []
        for n in queue:
            visited[n] = True
            if n == K:
                count += 1
            else:
                if n - 1 >= 0 and visited[n-1] is False:
                    cases.append(n-1)
                if n + 1 <= K + 1 and visited[n+1] is False:
                    cases.append(n+1)
                if n * 2 <= K + 1 and visited[n*2] is False:
                    cases.append(n*2)
        if count != 0:
            return depth, count
        queue = cases
        depth += 1


def solution():
    N, K = map(int, input().split())
    depth, count = bfs(N, K)
    print(depth, count, sep='\n')


solution()




# def bfs(N, K):
#     visited = [0 for i in range(100001)]
#     queue = [N]
#     depth, count = 0, 0
#
#     if N >= K:
#         return N-K, 1
#
#     while queue:
#         cases = []
#         for n in queue:
#             visited[n] = True
#             if n == K:
#                 count += 1
#             else:
#                 if n - 1 >= 0:
#                     if visited[n-1] == 0 or visited[n-1] == visited[n] + 1:
#                         visited[n-1] = visited[n] + 1
#                         cases.append(n-1)
#                 if n + 1 <= K + 1:
#                     if visited[n+1] == 0 or visited[n+1] == visited[n] + 1:
#                         visited[n+1] = visited[n] + 1
#                         cases.append(n+1)
#                 if n * 2 <= K + 1:
#                     if visited[n*2] == 0 or visited[n*2] == visited[n] + 1:
#                         visited[n*2] = visited[n] + 1
#                         cases.append(n*2)
#         if count != 0:
#             return depth, count
#         queue = cases
#         depth += 1
#
#
# def solution():
#     N, K = map(int, input().split())
#     depth, count = bfs(N, K)
#     print(depth, count, sep='\n')
#
#
# solution()
#
