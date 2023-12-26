N = int(input())
S = input()

T = "atcoder"

MOD = 10 ** 9 + 7


def add(a, b):
    a += b
    if a >= MOD:
        a -= MOD
    return a


dp = [[0] * (len(T) + 1) for _ in range(N + 1)]

dp[0][0] = 1

for i in range(N):
    for j in range(len(T) + 1):
        dp[i + 1][j] = add(dp[i + 1][j], dp[i][j])

        if j < len(T) and S[i] == T[j]:
            dp[i + 1][j + 1] = add(dp[i + 1][j + 1], dp[i][j])

print(dp[N][len(T)])
