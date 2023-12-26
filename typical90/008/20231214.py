N = int(input())
S = input()

MOD = 10 ** 9 + 7

GOAL_STRING = "atcoder"

# 足すたびにあまり求める関数
def add(a, b):
    a += b
    if a >= MOD:
        a -= MOD
    return a

# dp[N-1][len(GOAL_STRING)]に求めたい通り数が納まる
dp = [[0] * (len(GOAL_STRING) + 1) for _ in range(N+1)]

# 遷移元の設定
dp[0][0] = 1

# 入力された文字列を一文字ずつ
for i in range(N):
    # "atcoder"を一文字ずつ
    for j in range(len(GOAL_STRING) + 1):
        # Noパターン
        dp[i+1][j] = add(dp[i+1][j], dp[i][j])
        # Yesパターン (まだ文字列が完成していなくて、対象文字を必要としている)
        if j < len(GOAL_STRING) and S[i] == GOAL_STRING[j]:
            dp[i+1][j+1] = add(dp[i+1][j+1], dp[i][j])


print(dp[N][len(GOAL_STRING)])
