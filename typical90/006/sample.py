# res[i][c] := i 文字目以降で最初に文字 c が登場する index
# 存在しないときは N
def calc_next(S):
    # 文字列 S の長さ
    N = len(S)

    # （Sの文字数 x 26(アルファベット数)）x （文字数 + 1）の配列
    res = [[N] * 26 for _ in range(N + 1)]

    # 各アルファベットがSの何文字目にあるかを調べる
    # 一文字ずつ見ていき、その文字を調査の開始地点とする（左に存在する文字は考慮しない）
    for current in range(N - 1, -1, -1):  # 文字列Sの最後の文字から探索する
        # アルファベットの位置情報は一つ右の文字のものを参照する
        for alphabet in range(26):
            res[current][alphabet] = res[current + 1][alphabet]

        # 位置情報を更新
        # 今まさに調べている文字の位置情報を更新。現在のインデックス番号を代入。
        res[current][ord(S[current]) - ord('a')] = current
        print(current)

    # 答えを返す
    return res


# 入力
N, K = map(int, input().split())
S = input()

# 前処理
res = ''
nex = calc_next(S)

# 貪欲法
# 最後に選んだ文字のインデックス番号
prev = -1
# 作りたい文字数分だけfor文を回す
for i in range(K):
    # 「a」を設定できないか確かめる。ダメなら「B」、「C」と順に。
    for alphabet in range(26):
        # 最後に選んだ文字より右にある望みのアルファベットのインデックス番号
        alphabet_index = nex[prev + 1][alphabet]

        # そのアルファベットを選ぶ場合のSの残り文字数
        s_rest = N - (alphabet_index + 1)
        # Kの残り文字数
        k_rest = K - (i + 1)
        # 文字数的に問題ないならそのアルファベットを選ぶ
        if s_rest >= k_rest:
            # ユニコードから文字に変換
            res += chr(ord('a') + alphabet)
            # 最後に選んだ文字のインデックス番号を書き換える
            prev = alphabet_index
            break
print(res)
