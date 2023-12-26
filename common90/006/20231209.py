# res[i][c] := i 文字目以降で最初に文字 c が登場する index
# 存在しないときは N
def calc_next(S):
    # 文字列 S の長さ
    N = len(S)

    # 答え
    res = [[N] * 26 for _ in range(N + 1)]

    # 後ろから見る
    for i in range(N - 1, -1, -1):
        # i + 1 文字目以降の結果を一旦 i 文字にコピー
        for j in range(26):
            res[i][j] = res[i + 1][j]

        # i 文字目の情報を反映させる
        res[i][ord(S[i]) - ord('a')] = i

    # 答えを返す
    return res

# 入力
N, K = map(int, input().split())
S = input()

# 前処理
res = ''
nex = calc_next(S)

# 貪欲法
j = -1
for i in range(K):
    for ordc in range(26):
        k = nex[j + 1][ordc]

        # ちゃんと K 文字が作れれば OK
        if N - k >= K - i:
            res += chr(ord('a') + ordc)
            j = k
            break
print(res)