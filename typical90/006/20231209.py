STRING_LENGTH, PART_STRING_LENGTH = map(int, input().split())
STRING = input()

ALPHABET_LENGTH = 26

ans = ""
prev_string_index = -1

# K個のアルファベットを決定する
# 「a」から順に対象として、文字列Sのどこにあるかを確認する
# 長さKの部分列を作るのに必要な長さを保てるのなら対象のアルファベットを選ぶ
# for part_string_index in range(PART_STRING_LENGTH):  # O(K)
#     # 「a」を0として、「z」までそれぞれ確認する
#     for alphabet_code in range(ALPHABET_LENGTH):  # O(M)
#         # 番号を文字に変換する
#         alphabet = chr(ord("a") + alphabet_code)
#         # 変換した文字がSのどこにあるか確認 (O(N))
#         try:
#             alphabet_index = STRING.index(alphabet, prev_string_index + 1)
#         except ValueError:
#             continue
#
#         s_rest = STRING_LENGTH - (alphabet_index + 1)
#         k_rest = PART_STRING_LENGTH - (part_string_index + 1)
#
#         # 文字数的に問題ないかチェック
#         if s_rest >= k_rest:
#             # OKならそのアルファベットを選ぶ
#             ans += alphabet
#             # 最後に選択した文字のインデックス番号を更新
#             prev_string_index = alphabet_index
#             # 当for分はこれで終了
#             break
#
# print(ans)


# 上記でACとなるがKxNは最大で100万回を超える

# 変換した文字がSのどこにあるか確認を別の方法でやる。
# 調査開始地点とアルファベットでインデックス番号を返却してくれるメモを用意する。←O(NxM)でいける
def get_string_index_dict(string, length, part_s_length):
    # メモの初期化
    # 各地点より右に文字列の内、どのアルファベットがSの中で何番目にあるかを記録
    # 初期値は全てSの長さとする。←存在するインデックス番号より大きい
    memo = [[length] * ALPHABET_LENGTH for _ in range(length + 1)]
    # Sを一文字ずつ見ていく
    # 一つ前で文字がなんだったか記憶するのと、重複文字のインデックス番号書き換えが必要だな
    # 後ろから見ていくか
    for i in range(length - 1, -1, -1):
        alphabet_code = ord(string[i]) - ord("a")
        # 一つ右の地点での記録をまずはコピー
        for alphabet in range(ALPHABET_LENGTH):
            memo[i][alphabet] = memo[i + 1][alphabet]
        # print(i)
        # print(memo[i])
        memo[i][alphabet_code] = i

    return memo


dict = get_string_index_dict(STRING, STRING_LENGTH, PART_STRING_LENGTH)

for part_string_index in range(PART_STRING_LENGTH):
    for alphabet in range(ALPHABET_LENGTH):
        target_alphabet_index = dict[prev_string_index+1][alphabet]
        s_rest = STRING_LENGTH - (target_alphabet_index + 1)
        k_rest = PART_STRING_LENGTH - (part_string_index + 1)
        if s_rest >= k_rest:
            ans += chr(ord("a") + alphabet)
            prev_string_index = target_alphabet_index
            break

print(ans)



