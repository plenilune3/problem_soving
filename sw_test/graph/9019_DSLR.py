from collections import deque
from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def bfs(begin, end):
    visited = [False for i in range(10000)]
    path = ''
    queue = deque([(begin, path)])

    while queue:
        register, path = queue.popleft()

        if register == end:
            return path
        else:
            register_D = (register * 2) % 10000
            if visited[register_D] is False:
                visited[register_D] = True
                queue.append((register_D, path + 'D'))
            register_S = 9999 if register == 0 else register - 1
            if visited[register_S] is False:
                visited[register_S] = True
                queue.append((register_S, path + 'S'))

            d1, d2d3d4 = divmod(register, 1000)
            L = d2d3d4 * 10 + d1
            if visited[L] is False:
                visited[L] = True
                queue.append((L, path + 'L'))
            d1d2d3, d4 = divmod(register, 10)
            R = d4 * 1000 + d1d2d3
            if visited[R] is False:
                visited[R] = True
                queue.append((R, path + 'R'))


def solution():
    T = int(input())

    for t in range(T):
        begin, end = map(int, input().split())

        answer = bfs(begin, end)
        print(answer + '\n')


solution()


# def D(x):
#     return x * 2 % 10000
#
#
# def S(x):
#     return x-1 if x else 9999
#
#
# def L(x):
#     q, r = divmod(x, 1000)
#     return r * 10 + q
#
#
# def R(x):
#     q, r = divmod(x, 10)
#     return r * 1000 + q
#
#
# def bfs(begin, end, C):
#     visited = [False for i in range(10000)]
#     path = [0 for i in range(10000)]
#     command = ['' for i in range(10000)]
#
#     visited[begin] = True
#     queue = deque([begin])
#
#     while queue:
#         register = queue.popleft()
#         if register == end:
#             route = []
#             while register != begin:
#                 route.append(command[register])
#                 register = path[register]
#             route.reverse()
#             return ''.join(map(str, route))
#         else:
#             register_next = (D(register), S(register), L(register), R(register))
#             for i in range(4):
#                 if visited[register_next[i]] is False:
#                     visited[register_next[i]] = True
#                     path[register_next[i]] = register
#                     command[register_next[i]] = C[i]
#                     queue.append(register_next[i])
#
#
# def solution():
#     T = int(input())
#
#     for t in range(T):
#         begin, end = map(int, input().split())
#         C = 'DSLR'
#
#         answer = bfs(begin, end, C)
#         print(answer + '\n')
#
#
# solution()

