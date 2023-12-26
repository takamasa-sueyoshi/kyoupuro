N, K = map(int, input().split())
S = input()

ALPHABET_LENGTH = 26


def get_alphabet_points(string):
    # メモの初期化
    memo = [[len(string)] * ALPHABET_LENGTH for _ in range(len(string) + 1)]
    # 対象の文字列を一文字ずつ見ていく
    # 対象の文字列を起点として、右にどのアルファベットが何番目に存在するか記録
    for i in range(len(string) - 1, -1, -1):
        # 一つ右の文字の記録をコピーし、探索中の文字列の位置情報のみ記録更新する(重複している場合に左の方が優先)
        memo[i] = memo[i + 1].copy()
        memo[i][ord(string[i]) - ord("a")] = i
    return memo


#  文字列S上の現在地点
current_on_s = 0

ans = ""

dict = get_alphabet_points(S)

# K個の文字列を作成
for i in range(K):
    # 「a」から順に「z」まで
    # 文字列Sのどこに存在するか。それを選んだ時にK個の文字列を作り得るのか
    for j in range(ALPHABET_LENGTH):
        # 文字列の位置情報を取得
        # 現在地点と検索したいアルファベットを渡す
        target = dict[current_on_s][j]

        # このアルファベットを選んだ場合の文字列Sの残り文字数
        rest_s = N - (target + 1)
        # 部分列の残り文字数
        rest_k = K - (i + 1)

        if rest_s >= rest_k:
            ans += chr(ord("a") + j)
            current_on_s = target + 1
            break

print(ans)
