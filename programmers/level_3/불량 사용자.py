from collections import defaultdict

cases = {}


def compare(user_id, banned_id):
    length_user_id = len(user_id)
    length_banned_id = len(banned_id)

    if length_user_id != length_banned_id:
        return False
    else:
        for i in range(length_user_id):
            if banned_id[i] == '*':
                continue
            elif user_id[i] != banned_id[i]:
                return False
        else:
            return True


def backtracking(depth, N, M, user_id, banned_id, index_user, index_banned, visited, result=None):
    global cases

    if result is None:
        result = []

    if depth == M:
        cases[' '.join(sorted(result))] = True
    else:
        for i in range(N):
            for j in range(index_banned, M):
                if visited[user_id[i]] is False and compare(user_id[i], banned_id[j]):
                    visited[user_id[i]] = True
                    result.append(user_id[i])
                    backtracking(depth + 1, N, M, user_id, banned_id, i + 1, j + 1, visited, result)
                    visited[user_id[i]] = False
                    result.pop()


def solution(user_id, banned_id):
    visited = defaultdict(lambda: False)

    backtracking(0, len(user_id), len(banned_id), user_id, banned_id, 0, 0, visited)

    answer = len(cases)
    return answer
