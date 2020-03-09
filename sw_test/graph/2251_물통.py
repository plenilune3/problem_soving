from collections import deque


def pour(x, y, queue, visited):
    if visited[x][y] is False:
        visited[x][y] = True
        queue.append((x, y))


def bfs(a, b, c, answer):
    visited = [[False for i in range(b+1)] for j in range(a+1)]
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        z = c - x - y

        if x == 0:
            answer.append(z)

        # x -> y
        water = min(x, b-y)
        pour(x-water, y+water, queue, visited)
        # x -> z
        water = min(x, c-z)
        pour(x-water, y, queue, visited)
        # y -> x
        water = min(y, a-x)
        pour(x+water, y-water, queue, visited)
        # y -> z
        water = min(y, c-z)
        pour(x, y-water, queue, visited)
        # z -> x
        water = min(z, a-x)
        pour(x+water, y, queue, visited)
        # z -> y
        water = min(z, b-y)
        pour(x, y+water, queue, visited)


def solution():
    A, B, C = map(int, input().split())
    answer = []

    bfs(A, B, C, answer)
    print(' '.join(map(str, sorted(answer))))


solution()


# def bfs(A, B, C, answer: set):
#     visited = {}
#     queue = deque([[0, 0, C]])
#     bottles_max = (A, B, C)
#
#     while queue:
#         a, b, c = queue.popleft()
#         state = 'A' + str(a) + 'B' + str(b) + 'C' + str(c)
#         visited[state] = True
#
#         if a == 0:
#             answer.add(c)
#
#         bottles_now = (a, b, c)
#         for i in range(3):
#             for j in range(3):
#                 if i == j or bottles_now[i] == 0:
#                     continue
#                 else:
#                     # i -> j
#                     state_next = [0, 0, 0]
#                     temp = bottles_now[i] + bottles_now[j]
#
#                     if temp >= bottles_max[j]:
#                         bottle_from = temp - bottles_max[j]
#                         bottle_to = bottles_max[j]
#                     else:
#                         bottle_from = 0
#                         bottle_to = temp
#
#                     state_next[i] = bottle_from
#                     state_next[j] = bottle_to
#                     state_next[3-(i+j)] = bottles_now[3-(i+j)]
#
#                     if visited.get('A' + str(state_next[0]) + 'B' + str(state_next[1]) + 'C' + str(state_next[2])) is None:
#                         queue.append(state_next)
#
#
# def solution():
#     A, B, C = map(int, input().split())
#     answer = set()
#     bfs(A, B, C, answer)
#     answer = list(answer)
#     answer.sort()
#     print(' '.join(map(str, answer)))
#
#
# solution()
