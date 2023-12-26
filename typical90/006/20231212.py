N, K = map(int, input().split())
S = input()

ALPHABET = 26


def get_alphabet_poinst(string, length):
    """
    :param string: マップ化したい文字列
    :param length: マップ化したい文字列の長さ
    :return: どのアルファベットがどの位置にあるかを記録したマップ
    """
    memo = [[length] * ALPHABET for _ in range(length + 1)]
    for i in range(length - 1, -1, -1):
        dict[i] = dict[i - 1].copy()
        alphabet_code = ord(string[i]) - ord("a")
        dict[i][alphabet_code] = i
    return memo


current = 0
ans = ""

memo = get_alphabet_poinst(S, N)

for i in range(K):
    for j in range(ALPHABET):
        # alphabet = chr(ord("a") + j)
        # try:
        #     alphabet_index = S.index(alphabet)
        # except:
        #     continue
        alphabet_index = memo[current][j]
        if S - (alphabet_index + 1) >= K - (i + 1):
            alphabet = chr(ord("a") + j)
            ans += alphabet
            current = alphabet_index + 1
            break

print(ans)
