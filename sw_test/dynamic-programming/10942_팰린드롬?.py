from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(4000000)

input = stdin.readline
print = stdout.write


def palindrome(S, E, numbers, dp):
    if dp[S][E] != '-1':
        return dp[S][E]
    elif S >= E:
        return '1'
    elif numbers[S] != numbers[E]:
        dp[S][E] = '0'
        return '0'
    else:
        dp[S][E] = palindrome(S+1, E-1, numbers, dp)
        return dp[S][E]


def solution(N, numbers, SE):
    dp = [['-1' for i in range(N)] for j in range(N)]

    for s, e in SE:
        answer = palindrome(s-1, e-1, numbers, dp)
        print(answer + '\n')


# def solution(N, numbers, SE):
#     dp = [[False for i in range(N)] for j in range(N)]
#
#     for i in range(N):
#         dp[i][i] = True
#         if i+1 < N and numbers[i] == numbers[i+1]:
#             dp[i][i+1] = True
#
#     for l in range(2, N):
#         for i in range(N-l):
#             if numbers[i] == numbers[i+l] and dp[i+1][i+l-1]:
#                 dp[i][i+l] = True
#
#     for S, E in SE:
#         if dp[S-1][E-1]:
#             print('1' + '\n')
#         else:
#             print('0' + '\n')


N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
SE = [tuple(map(int, input().split())) for m in range(M)]

solution(N, numbers, SE)

