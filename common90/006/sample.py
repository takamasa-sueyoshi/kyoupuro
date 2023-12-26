# res[i][c] := i 文字目以降で最初に文字 c が登場する index
# 存在しないときは N
def calc_next(S):
    # 文字列 S の長さ
    N = len(S)

    # （Sの文字数 x 26(アルファベット数)）x （文字数 + 1）の配列
    res = [[N] * 26 for _ in range(N + 1)]

    # 文字列Sの最後の文字から探索する
    for i in range(N - 1, -1, -1):
        print(i)
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
