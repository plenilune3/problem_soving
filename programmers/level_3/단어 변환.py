from collections import deque


def solution(begin, target, words):
    answer = 0
    queue = deque([(list(begin), 0)])
    N = len(begin)
    visited = dict()

    while queue:
        now, depth = queue.popleft()

        if ''.join(now) == target:
            return depth

        for i in range(N):
            for j in range(97, 123):
                temp = now[:]

                if temp[i] != chr(j):
                    temp[i] = chr(j)
                    word = ''.join(temp)

                    if word in words and visited.get(word) is None:
                        visited[word] = True
                        queue.append((temp, depth + 1))

    return answer

