N = int(input())
numbers = list(map(int, input().split()))
operator_count = list(map(int, input().split()))
sum_max = float('-inf')
sum_min = float('inf')


def dfs(depth, N, numbers, result, addition, subtraction, multiplication, division):
    global sum_max, sum_min

    if depth == N:
        sum_max = max(sum_max, result)
        sum_min = min(sum_min, result)
    else:
        if addition:
            dfs(depth + 1, N, numbers, result + numbers[depth], addition - 1, subtraction, multiplication, division)
        if subtraction:
            dfs(depth + 1, N, numbers, result - numbers[depth], addition, subtraction - 1, multiplication, division)
        if multiplication:
            dfs(depth + 1, N, numbers, result * numbers[depth], addition, subtraction, multiplication - 1, division)
        if division:
            temp = result // numbers[depth] if result > 0 else -(-result // numbers[depth])
            dfs(depth + 1, N, numbers, temp, addition, subtraction, multiplication, division - 1)


def solution(N, numbers, operator_count):
    dfs(1, N, numbers, numbers[0],  *operator_count)
    print(sum_max)
    print(sum_min)


solution(N, numbers, operator_count)

