
def solution():
    dp = [0 for i in range(5001)]
    dp[0] = 1

    for i in range(2, 5001, 2):
        for j in range(2, i+1, 2):
            dp[i] += (dp[j-2] * dp[i-j]) % 1000000007

    return dp


T = int(input())
dp = solution()

for t in range(T):
    L = int(input())
    print(dp[L] % 1000000007)

