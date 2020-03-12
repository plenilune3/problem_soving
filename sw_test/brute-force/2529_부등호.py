K = int(input())
inequality = input().split()
visited = [False for i in range(10)]
cases = []


def possible(i, j, op):
    if op == '<':
        if i < j:
            return True
        else:
            return False
    elif op == '>':
        if i > j:
            return True
        else:
            return False


def backtracking(depth, N, result=[]):
    if depth == N:
        cases.append(result.copy())
    else:
        for i in range(10):
            if visited[i] is False:
                if depth == 0 or possible(result[-1], i, inequality[depth-1]):
                    visited[i] = True
                    result.append(i)
                    backtracking(depth+1, N, result)
                    visited[i] = False
                    result.pop()


backtracking(0, K+1)
print(''.join(map(str, cases[-1])))
print(''.join(map(str, cases[0])))
